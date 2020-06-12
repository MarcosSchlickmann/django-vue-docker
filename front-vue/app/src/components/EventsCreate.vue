<template>
	<form>
		<v-text-field
			v-model="event.title"
			label="Title"
			required
		></v-text-field>

		<v-textarea
			v-model="event.description"
			label="Description"
			counter
		></v-textarea>

		<v-row>
			<v-col >
				<v-row>
					<v-col>
						<v-menu
							ref="menu_start_date"
							v-model="menu_start_date"
							:close-on-content-click="false"
							:return-value.sync="event.start_date"
							transition="scale-transition"
							offset-y
							min-width="290px"
						>
							<template v-slot:activator="{ on, attrs }">
								<v-text-field
									v-model="event.start_date"
									label="Start date"
									prepend-icon="mdi-calendar"
									readonly
									v-bind="attrs"
									v-on="on"
								></v-text-field>
							</template>
							<v-date-picker v-model="event.start_date" no-title scrollable>
								<v-spacer></v-spacer>
								<v-btn text color="primary" @click="menu_start_date = false">Cancel</v-btn>
								<v-btn text color="primary" @click="$refs.menu_start_date.save(event.start_date)">OK</v-btn>
							</v-date-picker>
						</v-menu>
					</v-col>
					<v-col>
						<v-menu
							ref="menu_start_time"
							v-model="menu_start_time"
							:close-on-content-click="false"
							:nudge-right="40"
							:return-value.sync="event.start_time"
							transition="scale-transition"
							offset-y
							max-width="290px"
							min-width="290px"
						>
							<template v-slot:activator="{ on, attrs }">
								<v-text-field
									v-model="event.start_time"
									label="Start time"
									prepend-icon="mdi-clock-outline"
									readonly
									v-bind="attrs"
									v-on="on"
								></v-text-field>
							</template>
							<v-time-picker
								v-if="menu_start_time"
								v-model="event.start_time"
								full-width
								format="24hr"
								@click:minute="$refs.menu_start_time.save(event.start_time)"
							></v-time-picker>
						</v-menu>
					</v-col>
				</v-row>
			</v-col>
			<v-col class="align-self-center" lg="1"> <v-icon class="w-100">mdi-arrow-right</v-icon> </v-col>
			<v-col >
				<v-row>
					<v-col>
						<v-menu
							ref="menu_finish_date"
							v-model="menu_finish_date"
							:close-on-content-click="false"
							:return-value.sync="event.finish_date"
							transition="scale-transition"
							offset-y
							min-width="290px"
						>
							<template v-slot:activator="{ on, attrs }">
								<v-text-field
									v-model="event.finish_date"
									label="Finish date"
									prepend-icon="mdi-calendar"
									readonly
									v-bind="attrs"
									v-on="on"
								></v-text-field>
							</template>
							<v-date-picker v-model="event.finish_date" no-title scrollable>
								<v-spacer></v-spacer>
								<v-btn text color="primary" @click="menu_finish_date = false">Cancel</v-btn>
								<v-btn text color="primary" @click="$refs.menu_finish_date.save(event.finish_date)">OK</v-btn>
							</v-date-picker>
						</v-menu>
					</v-col>
					<v-col>
						<v-menu
							ref="menu_finish_time"
							v-model="menu_finish_time"
							:close-on-content-click="false"
							:nudge-right="40"
							:return-value.sync="event.finish_time"
							transition="scale-transition"
							offset-y
							max-width="290px"
							min-width="290px"
						>
							<template v-slot:activator="{ on, attrs }">
								<v-text-field
									v-model="event.finish_time"
									label="Finish time"
									prepend-icon="mdi-clock-outline"
									readonly
									v-bind="attrs"
									v-on="on"
								></v-text-field>
							</template>
							<v-time-picker
								v-if="menu_finish_time"
								v-model="event.finish_time"
								full-width
								format="24hr"
								@click:minute="$refs.menu_finish_time.save(event.finish_time)"
							></v-time-picker>
						</v-menu>
					</v-col>
				</v-row>
			</v-col>
		</v-row>

		<v-text-field
			v-model="event.address"
			label="Address"
			required
		></v-text-field>		

		<v-btn class="mr-4" @click="submit">submit</v-btn>
		<v-btn @click="clear">clear</v-btn>
	</form>
</template>

<script>
import axios from 'axios'
import { eventBus } from '../main'


export default {

	name: 'EventsCreate',

	data () {
		return {
			event: {
				title: '',
				description: '',
				start_date: '',
				start_time: '',
				finish_date: '',
				finish_time: '',
				
				address: '',
			},
			menu_start_date: '',
			menu_start_time: '',
			menu_finish_date: '',
			menu_finish_time: '',
		}
	},
	methods: {
		clear(){
			this.event.title = ''
			this.event.description = ''
			this.event.start_date = ''
			this.event.start_time = ''
			this.event.finish_date = ''
			this.event.finish_time = ''
			this.event.address = ''
		},
		submit(){
			axios.post(process.env.VUE_APP_BASE_URL + '/events/', {
				title: this.event.title,
				description: this.event.description,
				start_date_time: this.event.start_date + ' ' + this.event.start_time,
				finish_date_time: this.event.finish_date + ' ' + this.event.finish_time,
				address: this.event.address,
			})
			.then(() => {
				eventBus.$emit('fetchEvents');
				this.clear();
			})
			
		}
	}
}
</script>

<style lang="css" scoped>
</style>