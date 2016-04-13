angular
  .module('web_application', [
    'web_application.config',
    // ...
  ]);

angular
  .module('web_application.config', []);

  /**
  * @name run
  * @desc Update xsrf $http headers to align with Django's defaults
  */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
