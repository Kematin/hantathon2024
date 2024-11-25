function handleClick() {
  console.log("CLICK!");
}

window.createListener = function () {
  const assistentComponent = document.querySelector("#assistent");
  assistentComponent.addEventListener("click", handleClick);
};
