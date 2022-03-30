# Aplicação web simples com Flask


## 🏁 Tópicos

<!--ts-->
   * [Rodando o projeto localmente](#rodando-o-projeto-localmente)
   * [Implantação do aplicativo para o gcloud appengine](#implantação-do-aplicativo-para-o-gcloud-appengine)
   * [Pré-requisitos](#pré-requisitos)
   * [Instalando o componente Gcloud App Engine Python](#instalando-o-componente-gcloud-app-engine-python)
   * [Criando um novo projeto](#criando-um-novo-projeto)
   * [Vinculando-se a um projeto existente](#vinculando-se-a-um-projeto-existente)
   * [Empurrando seu aplicativo para a Nuvem do Google](#empurrando-seu-aplicativo-para-a-nuvem-do-google)
<!--te-->


### Rodando o projeto localmente

#### Na raiz do projeto executar:

     pip install -r requirements.txt

     python main.py

* Acesso ao front end: http://localhost:5000



### Implantação do aplicativo para o gcloud appengine

#### Pré-requisitos:

* SDK gcloud atualizado instalado no seu sistema: https://cloud.google.com/sdk/install

* Componente Gcloud App Engine Python

* Projeto gcloud criado e vinculado

#### Instalando o componente Gcloud App Engine Python:

A partir do Google Cloud SDK Shell (iniciado com permissões administrativas)

     gcloud components install app-engine-python

#### Criando um novo projeto:

Se você ainda não criou um projeto gcloud, você pode fazer isso a partir de https://console.cloud.google.com ou da linha de comando de seus computadores usando o SDK. Se você já criou o projeto via https://console.cloud.google.com você precisará realizar a vinculação a um projeto existente. Se, em vez disso, você usar a linha de comando SDK em seu computador, isso será feito para você.

     gcloud create project PROJECT-NAME

substituindo o PROJECT-NAME pelo nome do seu próprio projeto.

##### Vinculando-se a um projeto existente:

De qualquer ferramenta de linha de comando\terminal

     gcloud config set project PROJECT-NAME

substituindo o PROJECT-NAME pelo nome do seu próprio projeto.

### Empurrando seu aplicativo para a Nuvem do Google:

Agora que seu ambiente local do Google foi configurado para apontar para o projeto app-engine correto, mude para sua pasta de projeto e digite o seguinte código em seu terminal local/shell/cli para empurrar seu projeto para o projeto em sua Conta Google Cloud.

     gcloud app deploy

Para ver seu aplicativo publicado, você pode usar o seguinte código em seu terminal/shell/cli

     gcloud app browse

Ou você pode visitar https://YOUR-PROJECT.appspot.com, substituindo seus projetos pelo seu próprio nome de projetos.