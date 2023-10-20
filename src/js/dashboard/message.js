function msgError(value = "", where = "") {
  let path = "";
  var message = `
  <div class="custom-alert" role="alert">
  <div class="media custom-alert-body">
    <span class="custom-alert-icon bg-danger text-white bx bx-x"></span>
  <div class="media-body custom-alert-content">
    <h6 class="custom-alert-heading"><b>Opps!</b> you got an error</h6>
    <p class="custom-alert-subheading">${value}</p>
  </div>
  <button class="bx bx-x  alert-close" onclick="parentNode.parentNode.parentNode.removeChild(parentNode.parentNode);"
  type="button" data-dismiss="alert"></button></p>
  </div>`;
  if (where == "") {
    path = "#response";
  } else {
    path = where;
  }
  $(path).html(message);
}

function msgSuccess(value = "", where = "") {
  let path = "";
  var message = `
  <div class="custom-alert success-alert" role="alert">
  <div class="custom-alert-body">
    <i class="bx bx-check custom-alert-icon bg-success text-white"></i>
  <div class="custom-alert-content">
    <h6 class="custom-alert-heading"><b>Congratulations!</b></h6>
    <p class="custom-alert-subheading">${value}</p>
  </div>
  <button class="bx bx-x alert-close" type="button" onclick="parentNode.parentNode.parentNode.removeChild(parentNode.parentNode);"
   data-dismiss="alert"></button></p>
  </div>`;
  if (where == "") {
    path = "#response";
  } else {
    path = where;
  }
  $(path).html(message);
  $(".success-alert").fadeOut(10000)
}


function reload() {
  setTimeout(function () {
    location.reload();
  }, 1000);
}
function redirect(location) {
  window.open(location, "_SELF");
}
