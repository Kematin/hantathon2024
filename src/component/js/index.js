// ---------------------------- VARIABLES ---------------------------------------

// MIC
let isEnabled = false;
let mediaRecorder = null;
let voice = [];
let stream = null;

// ---------------------------- RECORD MIC ---------------------------------------

//     /\_/\           ___
//    = o_o =_______    \ \
//     __^      __(  \.__) )
// (@)<_____>__(_____)____/

export function createListener() {
  const assistentComponent = document.querySelector("#assistent");

  assistentComponent.addEventListener("click", async () => await handleClick());
}

async function handleClick() {
  if (!stream) {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  }

  if (!mediaRecorder) {
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.addEventListener("dataavailable", (event) => {
      voice.push(event.data);
    });

    mediaRecorder.addEventListener("stop", () => {
      stopRecord();
    });
  }

  if (!isEnabled) {
    mediaRecorder.start();
    console.log("Recording started");
  } else {
    mediaRecorder.stop();
    console.log("Recording stopped");
  }

  isEnabled = !isEnabled;
}

function stopRecord() {
  console.log("Recording stopped. Audio data available:", voice);
  const audioBlob = new Blob(voice, { type: "audio/webm" });

  const reader = new FileReader();
  reader.onloadend = function () {
    const arrayBuffer = reader.result;
    const byteArray = new Uint8Array(arrayBuffer);

    voice = [];
    command = getCommand(byteArray);
    executeCommand(command);
  };
  reader.readAsArrayBuffer(audioBlob);
}

function getCommand(byteArray) {
  console.log("Byte Array:", byteArray);

  const base64Voice = arrayBufferToBase64(byteArray.buffer);

  const payload = {
    voice: base64Voice,
  };

  fetch(`${API_HOST}:${API_PORT}/api/command`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("API Response:", data);
    })
    .catch((error) => {
      console.error("Error sending request:", error);
    });
}

function arrayBufferToBase64(buffer) {
  const binary = String.fromCharCode.apply(null, new Uint8Array(buffer));
  return window.btoa(binary);
}

// ---------------------------- HANDLE COMMAND ---------------------------------------

//        .
//       ":"
//     ___:____     |"\/"|
//   ,'        `.    \  /
//   |  O        \___/  |
// ~^~^~^~^~^~^~^~^~^~^~^~^~

export function executeCommand(command) {
  console.log(`EXECUTE ${command}`);
}
