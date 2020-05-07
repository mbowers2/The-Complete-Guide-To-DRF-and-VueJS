Vue.component('comment', {
    props: {
        comment: {
            type: Object,
            required: true
        }
    },
    template: `
        <div>
            <div class="card-body">
                <p>{{ comment.username }}</p>
                <p>{{ comment.content }}</p>
            </div>
            <hr>
        </div>
    `
})

const app = new Vue({
    el: '#app',
    data: {
        comments: [
            {
                username: 'geoff',
                content: 'first!'
            },
            {
                username: 'carl',
                content: 'Second :|'
            },
            {
                username: 'steve',
                content: 'last :('
            }
        ]
    }
});