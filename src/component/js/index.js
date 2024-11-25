function handleClick() {
  console.log("CLICK!");
}

export function createListener() {
  const assistentComponent = document.querySelector("#assistent");
  assistentComponent.addEventListener("click", handleClick);
}
