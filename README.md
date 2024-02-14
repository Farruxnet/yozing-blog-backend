# Install

## Step 1: Run docker compose
```bash
docker compose up -d
```

## Step 2: Install pip packages
```bash
pip install -r requirements.txt
```

## Step 3: Load fixtures data
```bash
python manage.py loaddata users
python manage.py loaddata helpers
python manage.py loaddata categries
python manage.py loaddata content
```

## Step 4: Load post data
```bash
python manage.py load_yozing
```


## Optional: Remove post data
```bash
python manage.py remove_yozing
```

## Generating Tags and Categories with ChatGPT-3.5

## Description
This project utilizes ChatGPT-3.5 to generate tags and categories for various content.

## Yozing Data
For the training data, you can use the dataset available on Kaggle: [Kun Uz Yangiliklar](https://www.kaggle.com/datasets/airiteam/kun-uz-yangiliklar). This dataset can be employed for Yozing (content generation) tasks.

## Dataset Information
- **Name:** Kun Uz Yangiliklar
- **Provider:** [Airiteam](https://www.kaggle.com/airiteam)
- **Link:** [Kun Uz Yangiliklar Dataset](https://www.kaggle.com/datasets/airiteam/kun-uz-yangiliklar)

Feel free to explore the dataset and use it to enhance the capabilities of your ChatGPT-3.5 model for generating tags and categories.
