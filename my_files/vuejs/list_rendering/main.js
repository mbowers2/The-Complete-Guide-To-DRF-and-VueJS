const app = new Vue({
    el: '#app',
    data: {
        users: ['geoff', 'carl', 'steve', 'joe', 'earl', 'clancy'],
        users2: [
            {
                id: 343,
                name: 'Geoff',
                profession: 'Loser',
            },
            {
                id: 234,
                name: 'carl',
                profession: 'lame',
            },
            {
                id: 4587,
                name: 'steve',
                profession: 'idiot',
            }
        ]
    }
});