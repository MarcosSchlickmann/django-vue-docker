<template>
	<div v-if="events">
		<template>
			<v-data-table
			:headers="events_headers"
			:items="events"
			:sort-by="['id']"
			:sort-desc="[true]"
			multi-sort
			class="elevation-1"
			></v-data-table>
		</template>
	</div>
</template>

<script>
import axios from 'axios';
import { eventBus } from '../main'

export default {

  name: 'EventsList',

  data: () => ({
    events: [],
    events_headers: [
      {text: '#', value: 'id'},
      {text: 'Title', value: 'title'},
      {text: 'Start', value: 'start_date_time'},
    ],
  }),
  methods: {
    getEvents(){
      axios.get(process.env.VUE_APP_BASE_URL + '/events/')
        .then(response => {
          this.events = response.data;
          let options = {
            year: 'numeric', month: 'numeric', day: 'numeric',
            hour: 'numeric', minute: 'numeric', second: 'numeric',
            hour12: false,
          }
          for (var id in this.events){
            this.events[id].start_date_time = new Intl.DateTimeFormat(
                'pt-BR', 
                options
              ).format(new Date(this.events[id].start_date_time));
          }
        })
    }
  },
  mounted () {
    this.getEvents();
  },
  created() {
    eventBus.$on('fetchEvents', () => {
      this.getEvents();
    })
  }
}
</script>

<style lang="css" scoped>
</style>