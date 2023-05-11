var student_object = {};

Array.from(
  document.querySelectorAll("table")[7].children[0].childNodes
).forEach((element, index) => {
  try {
    is_checkbox = element.children[0].children[0].type;
    if (is_checkbox === "checkbox") {
      links = element.children[5].children[0].href;
      code = links.split("&")[5].split("=")[1];
      student_code = element.children[1].innerText;
      student_object[student_code] = code;
    }
  } catch (error) {
    er = error;
  }
});
