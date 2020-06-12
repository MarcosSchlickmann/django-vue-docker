<template>
  <v-app>

    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          class="mb-6"
          justify="center"
          no-gutters
        >
          <v-col lg="6">
            <EventsCreate/>
          </v-col>
        </v-row>
        <v-divider></v-divider>
        <v-row
          class="mb-6"
          justify="center"
          no-gutters
        >
          <v-col lg="6">
            <EventsList/>
          </v-col>
        </v-row>
        
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import EventsCreate from './components/EventsCreate';
import EventsList from './components/EventsList';


export default {
  name: 'App',

  components: {
    EventsCreate,
    EventsList,
  },

  
};
</script>
