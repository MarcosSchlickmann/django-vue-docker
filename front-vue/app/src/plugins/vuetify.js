import '@mdi/font/css/materialdesignicons.css';
import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import en from 'vuetify/es5/locale/en';

Vue.use(Vuetify);

export default new Vuetify({
    lang: {
      locales: { en },
      current: 'en',
    },
    icons: {
      iconfont: 'mdi',
    }
});
