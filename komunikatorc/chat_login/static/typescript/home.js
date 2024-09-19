new Vue({
  el: '#app',
  data: {
    messages: [],
    newMessage: '',
    from: null, // For loading previous messages
  },


  methods: {
    loadMessages() {
      axios.post('/chat/api/messages/latest/', { batch_size: 25 })
        .then(response => {
          this.messages = response.data.messages;
        });
    },
    loadMoreMessages() {
      axios.post('chat/api/messages/previous/', { from: this.from, batch_size: 25 })
        .then(response => {
          this.messages = [...response.data.messages, ...this.messages];
        });
    },
    sendMessage() {
      axios.post('chat/api/messages/send/', {
        group_id: 1,
        body: this.newMessage,
      }).then(() => {
        this.newMessage = '';
        this.loadMessages();
      });
    }
  },
  mounted() {
    this.loadMessages();
  }
});