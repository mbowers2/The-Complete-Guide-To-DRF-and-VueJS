// Remaining tasks counter
Vue.component('remain-tasks', {
    props: {
        remainTasks: Number
    },
    template: `
        <div class="lead">
            Remaining tasks: {{ remainTasks }}
        </div>
    `
})

// Task input
Vue.component('task-input', {
    data: function() {
        return {
            new_task: null
        }
    },
    template: `
        <form @submit.prevent="addTask" class="form mt-2">
            <div class="form-group">
                <input type="text"
                       class="form-control"
                       v-model="new_task"
                       @keup.enter="submit"
                       placeholder="What do you need to do?"
                > 
            </div>
        </form>
    `,
    methods: {
        addTask: function() {
            if (this.new_task){
                this.$emit('add-task', this.new_task);
                this.new_task = null;
            }
        }
    }
})

// Task
Vue.component('single-task', {
    props: {
        task: String
    },
    template: `
        <div class="alert alert-success">
            {{ task }}
            <button type="button" 
                    class="close no-outline" 
                    @click="removeTask">
            <span aria-hidden="true">&times;</span>
            </button>
        </div>
    `,
    methods: {
        removeTask: function(task) {
            this.$emit('remove-task', this.task)
        }
    }
})

// Task list
Vue.component('task-list', {
    props: {
        tasks: Array,
        removeCallback: Function
    },
    template: `
        <div>
            <p v-if="tasks.length === 0">
            To add a new task write and press Enter.
            </p>
            <single-task
                v-else
                v-for="(task, index) in tasks"
                :task="task"
                :key="index"
                @remove-task="removeCallback"
            ></single-task>
        </div>
    `
})

var app = new Vue({
    el: '#app',
    data: {
        tasks: []
    },
    computed: {
        numTasks: function() {
            return this.tasks.length;
        }
    },
    methods: {
        addNewTask: function(new_task) {
            this.tasks.push(new_task);
        },
        removeCompletedTask: function(completed_task) {
            var index = this.tasks.indexOf(completed_task);
            this.tasks.splice(index, 1);
        }
    }
})