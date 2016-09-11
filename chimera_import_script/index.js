import jsonfile from 'jsonfile';
import http from 'http';

import concat from 'concat-stream';
import S from 'string';
import sanitizeHtml from 'sanitize-html';

const CHIMERA_API_URL_PREFIX = 'http://dusken.no/radio/api';
const PAPPAGORG_ON_DEMAND_URL = 'http://pappagorg.radiorevolt.no/v1/lyd/ondemand';
const PAPPAGORG_PODCAST_URL = 'http://pappagorg.radiorevolt.no/v1/lyd/podcast';

const OUTPUT_FILE = 'data.json';

const pappagorgDateToISOString = date => {
  const year = date.substr(0,4);
  const month = date.substr(4,2);
  const day = date.substr(6, 2);

  return (new Date(`${year}-${month}-${day}`)).toISOString();
}

const downloadAndParseJSON = function(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      res.setEncoding('utf8');
      res.on('error', reject);
      res.pipe(concat(resolve));
    });
  }).then(JSON.parse);
};

const downloadPrograms = downloadAndParseJSON.bind(undefined, `${CHIMERA_API_URL_PREFIX}/shows/?format=json`);

const resultJson = [];

const run = async () => {
  const programs = await downloadPrograms();
  let showIndex = 0;
  let episodeIndex = 0;

  for(const p of programs) {

    console.log(p.name);

    showIndex += 1;

    let imageurl = "";
    if(p.name == "Bankebrett") {
      imageurl = p.image;
    }
    else {
      imageurl = `${p.image.replace("thumbs/", "").split(".170x170_q85_crop_upscale.jpg").join("").split(".170x170_q85_crop_upscale.png").join("")}`;
    }

    const pdescription = sanitizeHtml(p.description, {
      allowedTags: [],
      allowedAttributes:[]
    });

    resultJson.push({
      model: 'data_models.show',
      pk: showIndex,
      fields: {
        name: p.name,
        slug: S(p.name).slugify().s,
        image: imageurl,
        archived: p.is_old,
        created_at: (new Date()).toISOString(),
        updated_at: (new Date()).toISOString(),
        content: pdescription,
        lead: p.lead.substr(0, 140)
      }
    });

    const podcastEpisodes = await downloadAndParseJSON(`${PAPPAGORG_PODCAST_URL}/${p.showID}`);
    const onDemandEpisodes = await downloadAndParseJSON(`${PAPPAGORG_ON_DEMAND_URL}/${p.showID}`);
    const chimeraEpisodes = await downloadAndParseJSON(p.episodes);

    let onlyPodcast = false;
    let episodes = onDemandEpisodes;

    if (onDemandEpisodes.lenght === 0 && podcastEpisodes.lenght !== 0) {
      onlyPodcast = true;
      episodes = podcastEpisodes;
    }

    for(const e of episodes) {
      episodeIndex += 1;

      let chimeraEpisode = chimeraEpisodes.find(ce => ce.broadcastID === e.id);
      if (onlyPodcast) {
        chimeraEpisode = chimeraEpisodes.find(ce => ce.podcast_url === e.url);
      }
      const podcastEpisode = podcastEpisodes.find(pe => pe.dato === e.dato);

      const date = pappagorgDateToISOString(e.dato.toString());

      let podcastUrl = '';
      let lead = '';
      let title = e.title;
      let onDemandUrl = e.url;
      let digasBroadcastId = e.id;

      if (onlyPodcast) {
        digasBroadcastId = 0;
      }

      if (chimeraEpisode) {
        podcastUrl = chimeraEpisode.podcast_url;
        lead = chimeraEpisode.lead;
        title = chimeraEpisode.headline;
      }

      if (onlyPodcast && !podcastUrl) {
        podcastUrl = e.url;
      }

      if (podcastEpisode && podcastUrl === '') {
        podcastUrl = podcastEpisode.url;
      }

      if (!podcastUrl) {
        podcastUrl = '';
      }

      lead = sanitizeHtml(lead, {
        allowedTags: [],
        allowedAttributes:[]
      });

      resultJson.push({
        model: 'data_models.episode',
        pk: episodeIndex,
        fields: {
          title: title,
          lead: lead.substr(0, 140),
          show: showIndex,
          created_at: date,
          updated_at: date,
          on_demand_url: onDemandUrl,
        }
      });
    }
  }
  jsonfile.writeFile(OUTPUT_FILE, resultJson, {spaces: 2}, function(err) {
    console.error(err)
  })
};

run();
