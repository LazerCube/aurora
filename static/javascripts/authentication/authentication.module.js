(function () {
  'use strict';

  angular
    .module('web_application.authentication', [
      'web_application.authentication.controllers',
      'web_application.authentication.services'
    ]);

  angular
    .module('web_application.authentication.controllers', []);

  angular
    .module('web_application.authentication.services', ['ngCookies']);
})();
