# Гайд по установке 

1. Клонирование репозитория
```bash
git clone https://gitlab.hackathon.uriit.ru/kematin2/11
cd ./11
```

2. Обучение NLP модели из готового датасета
```bash
cd train
python3.12 -m venv venv
. venv/bin/activate

(venv) pip install -r requirements.txt
(venv) python train.py
(venv) deactivate

# Перенесите лучшую эпоху в src (7.0)
mv hmao_model/checkpoint-364 ../src/ai_hmao_model
cd ..
```

3. Запуск вебсервера
```bash
# Заполните .env 
vim .env

poetry shell
(hackathon) poetry install
(hackathon) python app.py
```

4. Внедрение Компонента на сайт

> Перейдите на сайт [карты Югры](https://pubweb.admhmao.ru/subjectmaps/MAP_SOCIAL_OBJ)
> Вставьте компонент component.html
> Импортируйте javascript с помощью import.js в консоли

```html
<style>
  #assistent {
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    margin-left: 10px;
  }
  .assistent {
    color: #337ab7;
    background-color: #F3F5FB;
    border-radius: 8px;
    width: 140px;
    height: 40px;
  }

  .assistent:hover {
    background-color: #E4ECFC;
  }

  .assistentActivated {
    cursor: pointer;
    align-items: center;
    display: flex;
    justify-content: center;
    color: #34c924;
    background-color: #e2faeb;
    border-radius: 8px;
    width: 140px;
    height: 40px;
    margin-left: 10px;
  }

  .assistentActivated:hover {
    background-color: #c9f5c4;
  }
</style>

<li role="tab" tabindex="0" ng-class="[{active: active, disabled: disabled}, classes]" class="assistent uib-tab nav-item ng-scope ng-isolate-scope" index="'search'" select="$ctrl.onTabSelect('search')" heading="Ассистент" id="assistent">
  <div>Ассистент</div>
</li> 
```

```js
// API_HOST, API_PORT, SECRET_KEY как в .env

const API_HOST = "http://localhost";
const API_PORT = 8000;
const SECRET_KEY = "SECRET";

import(`${API_HOST}:${API_PORT}/api/js`)
  .then((module) => {
    module.createListener();
  })
  .catch((error) => console.error("Error loading module:", error));

```

### Готово !