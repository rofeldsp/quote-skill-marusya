const { pick } = require("ramda");


module.exports = {
  answer: function ({ request, session, version }, quote, author) {
      return {
          response: {
              text: quote + (author !== '' ? '\n\n— ' + author : ''),
              tts: quote + (author !== '' ? '\n\n— ' + author : ''),
              end_session: true
          },
          session: pick(["session_id", "message_id", "user_id"], session),
          version
      };
  },
};
