# Autoreply-Bot
This is the final project of the course "Deep Learning Programming in Fintech Practices(II)" (Course No. 517151), Spring 2023, NYCU, Hsinchu, Taiwan.

 
# Project Overview

The Autoreply-Bot is a deep learning-based chatbot that can automatically reply to user messages. The chatbot is trained on a large dataset, `PaddlePaddle`, and being fine-tuned with customized data.

With the given pretrained model from `PaddlePaddle`, along with the labeled data we generated massively with the help of ChatGPT, the model is able to be fine-tuned and do passage classifying. In this particular case, there are five common cases in milk powder customers' complaint, that are "hair", "piece", "rust", "caking" and "bug".

# Implementation

Connected to LINE, we created a official LINE bot that take users' text messages in to backend server, which is run on a fixed-ip host, and pre-process the text message, let the model classify which kind of complaint it is.

Regarding the pre-processing part, we use `mtranslate` to translate Chinese (Traditional) to Chinese (Simplified). This is because `PaddlePaddle` is trained on the basis of Chinese（Simplified）and the loss between the conversion of the two is extremely low.

As for the fine-tuning part, we directly use functions provided by `PaddlePaddle` dedicated to do fine-tuning. We generate some complaints on our own and let ChatGPT generate massive similar complaints, but with many kind of variations. Then we labeled the data in the way provided by the `PaddlePaddle` documentation.

After classifying, the model will choose the correct pre-generated response and send back to the LINE bot. Users will obtain corresponding wholesome responses in just a few seconds.

# Running server

To put the chat bot online, `run_server.py` is to be run in a terminal, and kept running. Plus, in this project, we used `Ngrok` to connect the host and the Line bot. Free plan of `Ngrok` already meets the needs of this project. Like the `run_server.py`, `Ngrok` needs to be kept running as long as you want the Line bot to respond to users. Note that everytime the `Ngrok` is restarted, the Webhook url in the Line bot API needs to be updated from the managing interface of LINE Developers.

# Project Goals

The main goal of the Autoreply-Bot project is to provide a highly efficient and effective chatbot that can automatically reply to user messages. The chatbot is able to understand the user's intent and generate a response that is contextually relevant to the user's message.


