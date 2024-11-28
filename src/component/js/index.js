// ---------------------------- VARIABLES ---------------------------------------

// Mic
let isEnabled = false;
let mediaRecorder = null;
let voice = [];
let stream = null;

// Commands
export function initCommands() {
  const commands = {
    site_info: siteInfoCommand,
    legend_info: legendInfoCommand,
    open_card: openCardCommand,
    disability_group: disablityGroupCommand,
    legend_place: legendPlaceCommand,
    search_radius: searchRadiusCommand,
    detailed_info: detailedInfoCommnad,
    path: searchPlaceCommand,
    search_place: searchPlaceCommand,
  };
  return commands;
}

// ---------------------------- RECORD MIC ---------------------------------------

//     /\_/\           ___
//    = o_o =_______    \ \
//     __^      __(  \.__) )
// (@)<_____>__(_____)____/

export function createListener() {
  const assistentComponent = document.querySelector("#assistent");
  if (assistentComponent === null) {
    console.warn("No assistent component");
  } else {
    assistentComponent.addEventListener(
      "click",
      async () => await handleClick()
    );
  }
}

async function handleClick() {
  const assistentComponent = document.querySelector("#assistent");

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
    assistentComponent.classList.remove("assistent");
    assistentComponent.classList.add("assistentActivated");
    assistentComponent.style.backgroundColor = "#e2faeb";
    mediaRecorder.start();
    console.log("Recording started");
  } else {
    assistentComponent.classList.remove("assistentActivated");
    assistentComponent.classList.add("assistent");
    assistentComponent.style.backgroundColor = "#F3F5FB";
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
    getCommand(byteArray);
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
      Authorization: `Bearer ${SECRET_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  })
    .then((response) => {
      if (!response.ok) {
        console.error(`API responded with status: ${response.status}`);
        executeNotFound();
      }
      return response.json();
    })
    .then((data) => {
      console.log("API Response:", data);
      if (data === false) {
        executeApiError();
      } else {
        executeCommand(data.command, data.data);
      }
    })
    .catch((error) => {
      console.error("Error sending request:", error);
      return false;
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

function executeCommand(command, data = null) {
  const func = getExecuteCommand(command);
  console.log(`Execute ${func}`);
  if (func === false) {
    executeNotFound();
  } else {
    if (data === null) {
      func();
    } else {
      func(data);
    }
  }
}

function getExecuteCommand(typeCommand) {
  try {
    const commands = initCommands();
    return commands[typeCommand];
  } catch (e) {
    return false;
  }
}

function executeApiError() {
  console.error("api error");
  playAudioDefault("api_error");
}

function executeNotFound() {
  console.error("command not found");
  playAudioDefault("not_found_error");
}

function executeNotFoundPlace() {
  console.error("place not found");
  playAudioDefault("place_not_found_error");
}

// ---------------------------- AUDIO WITH API LOGIC ------------------------------------

//              _.-````'-,_
//    _,.,_ ,-'`           `'-.,_
//  /)     (\                   '``-.
// ((      ) )                      `\
//  \)    (_/                        )\
//   |       /)           '    ,'    / \
//   `\    ^'            '     (    /  ))
//     |      _/\ ,     /    ,,`\   (  "`
//      \Y,   |  \  \  | ````| / \_ \
//        `)_/    \  \  )    ( >  ( >
//                 \( \(     |/   |/
//     lam & kem  /_(/_(    /_(  /_(

function playAudioDefault(filename) {
  fetch(`${API_HOST}:${API_PORT}/api/default/${filename}`, {
    headers: {
      Authorization: `Bearer ${SECRET_KEY}`,
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Audio file not found");
      }
      return response.blob();
    })
    .then((audioBlob) => {
      const audioUrl = URL.createObjectURL(audioBlob);

      const audio = new Audio(audioUrl);

      audio.play();
    })
    .catch((error) => {
      console.error("Error playing audio:", error);
    });
}

function playAudioCommand(text) {
  fetch(`${API_HOST}:${API_PORT}/api/speech`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${SECRET_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to convert text to speech");
      }
      return response.json();
    })
    .then((data) => {
      const base64Audio = data.content;

      const binaryString = atob(base64Audio);
      const byteArray = new Uint8Array(binaryString.length);

      for (let i = 0; i < binaryString.length; i++) {
        byteArray[i] = binaryString.charCodeAt(i);
      }

      const audioBlob = new Blob([byteArray], { type: "audio/mpeg" });
      const audioUrl = URL.createObjectURL(audioBlob);

      const audio = new Audio(audioUrl);
      audio.play();
    })
    .catch((error) => {
      console.error("Error playing audio:", error);
    });
}

// ---------------------------- MAIN JS LOGIC ------------------------------------

//            .--._.--.
//           ( O     O )
//           /   . .   \
//          .`._______.'.
//         /(           )\
//       _/  \  \   /  /  \_
//    .~   `  \  \ /  /  '   ~.
//   {    -.   \  V  /   .-    }
// _ _`.    \  |  |  |  /    .'_ _
// >_       _} |  |  | {_       _<
//  /. - ~ ,_-'  .^.  `-_, ~ - .\
//          '-'|/   \|`-`

function activateTab(tabHeading) {
  const tabs = document.querySelectorAll("li[role='tab']");

  tabs.forEach((tab) => {
    if (tab.getAttribute("heading") === tabHeading) {
      tab.classList.add("active");

      const link = tab.querySelector("a");
      if (link) {
        const clickEvent = new MouseEvent("click", {
          bubbles: true,
          cancelable: true,
        });
        link.dispatchEvent(clickEvent);
      }
    } else {
      tab.classList.remove("active");
    }
  });
}

function openLegendPage() {
  activateTab("Легенда");
}

function openCardPage() {
  activateTab("Поиск");
}

function getFormattedInfoRows(rows, indices) {
  let i = 0;
  const formattedInfo = indices.map((index) => {
    i++;
    const row = rows[index - 1];
    if (row) {
      const [key, value] = row.innerText.split("\t");
      return `${i}. ${key.trim()}: ${value.trim()}`;
    }
    return null;
  });

  return formattedInfo.filter(Boolean).join("\n");
}

function handleLegendPlace(place) {
  const clickEvent = new MouseEvent("click", {
    bubbles: true,
    cancelable: true,
  });
  const enterEvent = new KeyboardEvent("keydown", {
    key: "Enter",
    code: "Enter",
    which: 13,
    keyCode: 13,
    bubbles: true,
  });
  const inputEvent = new Event("input", { bubbles: true });

  const popupElement = document.querySelector(
    "a[placeholder='Выберите населенный пункт']"
  );
  const inputElement = document.querySelector(
    "input[aria-label='Выберите населенный пункт']"
  );

  popupElement.dispatchEvent(clickEvent);

  inputElement.value = place;
  inputElement.dispatchEvent(inputEvent);

  inputElement.dispatchEvent(enterEvent);
}

function getElementByXPath(xpath) {
  const result = document.evaluate(
    xpath,
    document,
    null,
    XPathResult.FIRST_ORDERED_NODE_TYPE,
    null
  );
  return result.singleNodeValue;
}

function waitForElement(xpath, timeout = 5000) {
  return new Promise((resolve, reject) => {
    const interval = 100;
    let elapsedTime = 0;

    const checkElement = () => {
      const element = getElementByXPath(xpath);
      const innerLi = element.querySelectorAll("li");
      if (innerLi.length >= 2) {
        resolve(innerLi);
      } else if (elapsedTime >= timeout) {
        reject(new Error("Element not found within timeout period"));
      } else {
        elapsedTime += interval;
        setTimeout(checkElement, interval);
      }
    };

    checkElement();
  });
}

function handleSearchInput(place) {
  const enterEvent = new KeyboardEvent("keydown", {
    key: "Enter",
    code: "Enter",
    which: 13,
    keyCode: 13,
    bubbles: true,
  });

  const inputEvent = new Event("input", { bubbles: true });

  const radioElement = document.querySelector("p.radio span.custom-radio");
  const searchElement = document.querySelector(
    "a[placeholder='Поставьте точку на карте или введите адрес']"
  );
  const searchInput = document.querySelector(
    "div.blockFind div.select2-search input[role='combobox']"
  );
  const listPopupSelector =
    "/html/body/main/subject-maps/div/social-page/div/div/div[1]/div[2]/div/div/div/div/div/div[3]/div[1]/div/ul";

  radioElement.click();
  searchElement.click();
  searchInput.click();

  searchInput.value = "";
  searchInput.dispatchEvent(inputEvent);

  return new Promise((resolve, reject) => {
    let currentPlace = place;

    function tryInput(place) {
      if (place.length === 2) {
        console.error("Unable to find a valid selection with the given input.");
        reject("No valid selection found");
        return;
      }

      searchInput.value = place;
      searchInput.dispatchEvent(inputEvent);

      waitForElement(listPopupSelector, 500)
        .then(() => {
          searchInput.dispatchEvent(enterEvent);
          resolve();
        })
        .catch(() => {
          tryInput(place.slice(0, -1));
        });
    }

    tryInput(currentPlace);
  });
}

function waitForTableAndSelectElement(isFirst = true) {
  const tableSelector = "div.k-grid-content tbody";
  const interval = 200;
  const maxWaitTime = 5000;
  let elapsedTime = 0;

  return new Promise((resolve, reject) => {
    const checkTable = setInterval(() => {
      const tableBody = document.querySelector(tableSelector);
      if (tableBody && tableBody.rows.length > 0) {
        clearInterval(checkTable);

        if (isFirst) {
          const firstRow = tableBody.rows[0];
          if (firstRow) {
            firstRow.click();
            resolve(firstRow);
          } else {
            reject(new Error("First row is undefined."));
          }
        } else {
          const allRows = Array.from(tableBody.rows);
          resolve(allRows);
        }
      }

      elapsedTime += interval;
      if (elapsedTime >= maxWaitTime) {
        clearInterval(checkTable);
        executeNotFoundPlace();
        reject(new Error("Table did not load in time."));
      }
    }, interval);
  });
}

// ---------------------------- INITIAL COMMANDS ------------------------------------

//                               __
//                      /\    .-" /
//                     /  ; .'  .'
//                    :   :/  .'
//                     \  ;-.'
//        .--""""--..__/     `.
//      .'           .'    `o  \
//     /                    `   ;
//    :                  \      :
//  .-;        -.         `.__.-'
// :  ;          \     ,   ;
// '._:           ;   :   (
//     \/  .__    ;    \   `-.
//  bug ;     "-,/_..--"`-..__)
//      '""--.._:

const siteInfoCommand = () => {
  playAudioDefault("site_info");
};

const legendInfoCommand = () => {
  openLegendPage();
  playAudioDefault("legend_info");
};

const openCardCommand = () => {
  openCardPage();
  playAudioDefault("open_card");
};

const disablityGroupCommand = () => {
  openCardPage();
  playAudioDefault("disablity_group");
};

const legendPlaceCommand = (data) => {
  openLegendPage();
  const place = data.place;
  handleLegendPlace(place);
  const formattedText = `Была найдена легенда для места ${data.place}`;
  playAudioCommand(formattedText);
};

const searchRadiusCommand = (data) => {
  playAudioDefault("wait");
  openCardPage();
  const place = data.place;
  handleSearchInput(place).then(() => {
    waitForTableAndSelectElement(false).then((allRows) => {
      if (!allRows || allRows.length === 0) {
        console.error("No rows found.");
        return;
      }

      let totalText = "Были найдены следующие объекты:\n";
      for (let i = 0; i < allRows.length; i++) {
        if (i === 2) {
          break;
        }
        const row = allRows[i];
        const [object, address] = row.innerText.split("\t");
        const formattedText = `${i + 1}. ${object} по адресу ${address}\n`;
        totalText += formattedText;
      }
      console.log(totalText);
      playAudioCommand(totalText);
    });
  });
};

const searchPlaceCommand = (data) => {
  if (data === undefined) {
    executeApiError();
    return;
  }
  openCardPage();
  const place = data.place;
  handleSearchInput(place).then(() => {
    waitForTableAndSelectElement().then((firstRow) => {
      const [object, address] = firstRow.innerText.split("\t");
      const formattedText = `Был найден объект ${object} по адресу ${address}`;
      playAudioCommand(formattedText);
    });
  });
};

const detailedInfoCommnad = (data) => {
  playAudioDefault("wait");
  openCardPage();
  const place = data.place;
  handleSearchInput(place).then(() => {
    waitForTableAndSelectElement().then((firstRow) => {
      const popupElement = document.querySelector(
        "div.leaflet-popup-content-wrapper"
      );
      const [object, address] = firstRow.innerText.split("\t");
      const objectInfo = `Был найден объект ${object} по адресу: ${address}`;
      if (popupElement === null) {
        executeNotFoundPlace();
      } else {
        let allInfo = popupElement.querySelectorAll(
          "tr.ng-scope:not(.ng-hide)"
        );
        const indicesToInclude = [4, 7, 9, 10, 11, 12, 13];
        const additionalInfo = getFormattedInfoRows(allInfo, indicesToInclude);
        const fullInfo = `${objectInfo}\n\nПодробная информация:\n${additionalInfo}`;
        console.log(fullInfo);
        playAudioCommand(fullInfo);
      }
    });
  });
};
