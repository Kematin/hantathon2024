function handleClick() {
  console.log("CLICK!");
}

function createListener() {
  const assistentComponent = document.querySelector("#assistent");
  assistentComponent.addEventListener("click", handleClick);
}
