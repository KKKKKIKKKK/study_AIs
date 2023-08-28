{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9eb9bb38-c5c1-42d7-b39c-876d947085ff",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b66fc512-d0f9-4ae1-b2c3-e738bb422827",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>diagnosis</th>\n",
       "      <th>radius_mean</th>\n",
       "      <th>texture_mean</th>\n",
       "      <th>perimeter_mean</th>\n",
       "      <th>area_mean</th>\n",
       "      <th>smoothness_mean</th>\n",
       "      <th>compactness_mean</th>\n",
       "      <th>concavity_mean</th>\n",
       "      <th>concave points_mean</th>\n",
       "      <th>...</th>\n",
       "      <th>texture_worst</th>\n",
       "      <th>perimeter_worst</th>\n",
       "      <th>area_worst</th>\n",
       "      <th>smoothness_worst</th>\n",
       "      <th>compactness_worst</th>\n",
       "      <th>concavity_worst</th>\n",
       "      <th>concave points_worst</th>\n",
       "      <th>symmetry_worst</th>\n",
       "      <th>fractal_dimension_worst</th>\n",
       "      <th>Unnamed: 32</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>842302</td>\n",
       "      <td>M</td>\n",
       "      <td>17.99</td>\n",
       "      <td>10.38</td>\n",
       "      <td>122.8</td>\n",
       "      <td>1001.0</td>\n",
       "      <td>0.11840</td>\n",
       "      <td>0.27760</td>\n",
       "      <td>0.3001</td>\n",
       "      <td>0.14710</td>\n",
       "      <td>...</td>\n",
       "      <td>17.33</td>\n",
       "      <td>184.6</td>\n",
       "      <td>2019.0</td>\n",
       "      <td>0.1622</td>\n",
       "      <td>0.6656</td>\n",
       "      <td>0.7119</td>\n",
       "      <td>0.2654</td>\n",
       "      <td>0.4601</td>\n",
       "      <td>0.11890</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>842517</td>\n",
       "      <td>M</td>\n",
       "      <td>20.57</td>\n",
       "      <td>17.77</td>\n",
       "      <td>132.9</td>\n",
       "      <td>1326.0</td>\n",
       "      <td>0.08474</td>\n",
       "      <td>0.07864</td>\n",
       "      <td>0.0869</td>\n",
       "      <td>0.07017</td>\n",
       "      <td>...</td>\n",
       "      <td>23.41</td>\n",
       "      <td>158.8</td>\n",
       "      <td>1956.0</td>\n",
       "      <td>0.1238</td>\n",
       "      <td>0.1866</td>\n",
       "      <td>0.2416</td>\n",
       "      <td>0.1860</td>\n",
       "      <td>0.2750</td>\n",
       "      <td>0.08902</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2 rows × 33 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       id diagnosis  radius_mean  texture_mean  perimeter_mean  area_mean  \\\n",
       "0  842302         M        17.99         10.38           122.8     1001.0   \n",
       "1  842517         M        20.57         17.77           132.9     1326.0   \n",
       "\n",
       "   smoothness_mean  compactness_mean  concavity_mean  concave points_mean  \\\n",
       "0          0.11840           0.27760          0.3001              0.14710   \n",
       "1          0.08474           0.07864          0.0869              0.07017   \n",
       "\n",
       "   ...  texture_worst  perimeter_worst  area_worst  smoothness_worst  \\\n",
       "0  ...          17.33            184.6      2019.0            0.1622   \n",
       "1  ...          23.41            158.8      1956.0            0.1238   \n",
       "\n",
       "   compactness_worst  concavity_worst  concave points_worst  symmetry_worst  \\\n",
       "0             0.6656           0.7119                0.2654          0.4601   \n",
       "1             0.1866           0.2416                0.1860          0.2750   \n",
       "\n",
       "   fractal_dimension_worst  Unnamed: 32  \n",
       "0                  0.11890          NaN  \n",
       "1                  0.08902          NaN  \n",
       "\n",
       "[2 rows x 33 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_BCW = pd.read_csv('../../../datasets/BreastCancerWisconsinDataSet.csv')\n",
    "df_BCW[:2]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eeeea098-32f1-49d1-a677-b8e3847dfc9a",
   "metadata": {
    "tags": []
   },
   "source": [
    "#### 과정(유방암DATASET)\n",
    "- 전처리 - 정형화 - 모델 교육 후 - 평가 서비스\n",
    "- 목표변수(diagnosis), 설명변수(*_mean 아닌 것) \n",
    "- 설명 \n",
    "    - diagnosis(유방종양의 진단결과 B(양성) , M(악성)\n",
    "    - perimeter_se(종양 경계면의 길이에 대한 표준오차값\n",
    "    - perimeter_worst(종양 경계면의 길이 최대값)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "930498b9-d0fe-4d97-aea1-aa401ebf5870",
   "metadata": {},
   "source": [
    "#### 1)  전처리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dbc00893-c2fb-4d9e-84c6-ec8ce1b0f792",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean',\n",
       "       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',\n",
       "       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',\n",
       "       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',\n",
       "       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',\n",
       "       'fractal_dimension_se', 'radius_worst', 'texture_worst',\n",
       "       'perimeter_worst', 'area_worst', 'smoothness_worst',\n",
       "       'compactness_worst', 'concavity_worst', 'concave points_worst',\n",
       "       'symmetry_worst', 'fractal_dimension_worst', 'Unnamed: 32'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_BCW.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4b0ab24f-c354-4e5a-a402-7019d0fe3c9a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "diagnosis          0\n",
       "perimeter_se       0\n",
       "perimeter_worst    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_BCW_extract = df_BCW[['diagnosis', 'perimeter_se', 'perimeter_worst']]\n",
    "df_BCW_extract.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d322624d-5ca1-4bd8-8f53-4e48fc25b833",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>diagnosis</th>\n",
       "      <th>perimeter_se</th>\n",
       "      <th>perimeter_worst</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>M</td>\n",
       "      <td>8.589</td>\n",
       "      <td>184.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>M</td>\n",
       "      <td>3.398</td>\n",
       "      <td>158.8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  diagnosis  perimeter_se  perimeter_worst\n",
       "0         M         8.589            184.6\n",
       "1         M         3.398            158.8"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 'diagnosis(유방종양의 진단결과)', 'perimeter_se', 'perimeter_worst'\n",
    "df_BCW_extract_preprocess = df_BCW_extract.dropna()\n",
    "df_BCW_extract_preprocess[:2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ca465540-936e-4ecd-adbc-275f6f11082e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "B    357\n",
       "M    212\n",
       "Name: diagnosis, dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_BCW_extract['diagnosis'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "ace6c8b8-9c84-4b56-b13f-9bd3d0b4c2a0",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# #종속변수는 diagnosis: Benign(양성), Malignancy(악성)\n",
    "# 양성이면 0 악성이면 1 그외2로 정제. \n",
    "def df_BCW(x):\n",
    "    if x == \"M\":\n",
    "        return 0\n",
    "    elif x == \"B\":\n",
    "        return 1\n",
    "    else:\n",
    "        return 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "8748d6de-e029-420f-8cda-9247d2db1e9b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\5-20\\AppData\\Local\\Temp\\ipykernel_19660\\819971798.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df_BCW_extract['label'] = df_BCW_extract['diagnosis'].apply(df_BCW)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>diagnosis</th>\n",
       "      <th>perimeter_se</th>\n",
       "      <th>perimeter_worst</th>\n",
       "      <th>label</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2</td>\n",
       "      <td>8.589</td>\n",
       "      <td>184.60</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>3.398</td>\n",
       "      <td>158.80</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>4.585</td>\n",
       "      <td>152.50</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>3.445</td>\n",
       "      <td>98.87</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2</td>\n",
       "      <td>5.438</td>\n",
       "      <td>152.20</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>564</th>\n",
       "      <td>2</td>\n",
       "      <td>7.673</td>\n",
       "      <td>166.10</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>565</th>\n",
       "      <td>2</td>\n",
       "      <td>5.203</td>\n",
       "      <td>155.00</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>566</th>\n",
       "      <td>2</td>\n",
       "      <td>3.425</td>\n",
       "      <td>126.70</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>567</th>\n",
       "      <td>2</td>\n",
       "      <td>5.772</td>\n",
       "      <td>184.60</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>568</th>\n",
       "      <td>2</td>\n",
       "      <td>2.548</td>\n",
       "      <td>59.16</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>569 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     diagnosis  perimeter_se  perimeter_worst  label\n",
       "0            2         8.589           184.60      2\n",
       "1            2         3.398           158.80      2\n",
       "2            2         4.585           152.50      2\n",
       "3            2         3.445            98.87      2\n",
       "4            2         5.438           152.20      2\n",
       "..         ...           ...              ...    ...\n",
       "564          2         7.673           166.10      2\n",
       "565          2         5.203           155.00      2\n",
       "566          2         3.425           126.70      2\n",
       "567          2         5.772           184.60      2\n",
       "568          2         2.548            59.16      2\n",
       "\n",
       "[569 rows x 4 columns]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_BCW_extract['label'] = df_BCW_extract['diagnosis'].apply(df_BCW)\n",
    "df_BCW_extract"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2174ea13-5c54-47d4-acf7-43e95c483f93",
   "metadata": {},
   "source": [
    "### 1. 정형화 단계 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "abf6c2e9-981b-40bd-9145-d2123337aec0",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((569,), (569, 2))"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "target_train = df_BCW_extract_preprocess['diagnosis']  # target_train = Y\n",
    "features_train = df_BCW_extract_preprocess[['perimeter_se', 'perimeter_worst']] # features_train = X \n",
    "target_train.shape, features_train.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0d246cc0-bd4e-486d-b775-ef7d177ef3e9",
   "metadata": {},
   "source": [
    "### 2. 모델 교육 및 학습"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "7550b31a-3aae-4846-a924-3802f6abf6ed",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LogisticRegression()"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "model = LogisticRegression()\n",
    "model.fit(features_train, target_train) # 모델훈련은 fit으로 진행. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "a0f08341-696f-4cf4-a480-f3e5c9f71ede",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([[0.48634477, 0.16479856]]), array([-19.32152776]))"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.coef_, model.intercept_"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a2f12e95-aa70-43fa-82fa-a0481037a91d",
   "metadata": {
    "tags": []
   },
   "source": [
    "### 3.예측"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "33a08a0d-443b-4d15-9ca2-bed153eeff2f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>diagnosis</th>\n",
       "      <th>perimeter_se</th>\n",
       "      <th>perimeter_worst</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>M</td>\n",
       "      <td>2.466</td>\n",
       "      <td>123.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>M</td>\n",
       "      <td>3.564</td>\n",
       "      <td>136.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>M</td>\n",
       "      <td>11.070</td>\n",
       "      <td>151.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>M</td>\n",
       "      <td>2.903</td>\n",
       "      <td>112.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>M</td>\n",
       "      <td>2.061</td>\n",
       "      <td>108.8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   diagnosis  perimeter_se  perimeter_worst\n",
       "10         M         2.466            123.8\n",
       "11         M         3.564            136.5\n",
       "12         M        11.070            151.7\n",
       "13         M         2.903            112.0\n",
       "14         M         2.061            108.8"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#미리 출력해보기 \n",
    "df_BCW_extract_preprocess[10:15] #위치가 인덱스가 features_train과 위치가 같다. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09ddb081-6e77-4f2f-9ea1-51d421d6e3a5",
   "metadata": {},
   "source": [
    "### 3-1 실제로 맞는것 0 12~14 = 3개 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "daa79ff3-31c5-40f3-af3d-13ccce8b017e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['M', 'M', 'M', 'M', 'B'], dtype=object)"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#평가에서 예측 \n",
    "model.predict(features_train[10:15])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "96496a43-67a8-49a1-9a8a-94354e8ddfe3",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[9.28047113e-02, 9.07195289e-01],\n",
       "       [7.34175433e-03, 9.92658246e-01],\n",
       "       [1.56934635e-05, 9.99984307e-01],\n",
       "       [3.66381947e-01, 6.33618053e-01],\n",
       "       [5.96063067e-01, 4.03936933e-01]])"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 확률적인 게임. \n",
    "# 왼쪽 0 (0.52=52%) >>>> 오른쪽 1(0.47=47%)\n",
    "model.predict_proba(features_train[10:15])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2df5c85a-f6c4-4d27-b3e6-d2585c95d6c6",
   "metadata": {},
   "source": [
    "### 4 .평가"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "d5d4ac24-340f-4561-8080-9e3f081ff98e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['M', 'M', 'M', 'B', 'M', 'B', 'M', 'M', 'B', 'B', 'M', 'M', 'M',\n",
       "       'M', 'B', 'M', 'M', 'M', 'M', 'B', 'B', 'B', 'M', 'M', 'M', 'M',\n",
       "       'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'B', 'M',\n",
       "       'B', 'B', 'B', 'M', 'M', 'B', 'M', 'B', 'B', 'B', 'B', 'B', 'B',\n",
       "       'B', 'M', 'M', 'B', 'M', 'M', 'B', 'B', 'B', 'B', 'M', 'B', 'M',\n",
       "       'M', 'B', 'B', 'B', 'B', 'M', 'B', 'M', 'B', 'B', 'M', 'B', 'M',\n",
       "       'M', 'B', 'B', 'B', 'M', 'M', 'B', 'M', 'M', 'M', 'B', 'M', 'B',\n",
       "       'B', 'B', 'B', 'M', 'M', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',\n",
       "       'B', 'B', 'B', 'B', 'M', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',\n",
       "       'M', 'M', 'M', 'B', 'M', 'M', 'B', 'B', 'B', 'M', 'M', 'B', 'M',\n",
       "       'B', 'M', 'M', 'M', 'M', 'B', 'B', 'B', 'M', 'B', 'B', 'M', 'B',\n",
       "       'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',\n",
       "       'M', 'M', 'B', 'B', 'B', 'M', 'M', 'B', 'M', 'B', 'B', 'M', 'M',\n",
       "       'B', 'B', 'M', 'M', 'B', 'B', 'B', 'B', 'M', 'B', 'B', 'M', 'M',\n",
       "       'M', 'B', 'M', 'B', 'M', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'M',\n",
       "       'B', 'M', 'M', 'M', 'M', 'B', 'M', 'M', 'M', 'B', 'M', 'B', 'M',\n",
       "       'B', 'M', 'M', 'B', 'M', 'M', 'M', 'B', 'B', 'B', 'M', 'M', 'B',\n",
       "       'B', 'B', 'M', 'B', 'M', 'B', 'M', 'B', 'B', 'M', 'B', 'B', 'M',\n",
       "       'B', 'B', 'M', 'M', 'B', 'M', 'B', 'B', 'B', 'B', 'M', 'B', 'B',\n",
       "       'B', 'B', 'B', 'M', 'B', 'M', 'M', 'M', 'B', 'M', 'M', 'M', 'M',\n",
       "       'M', 'M', 'M', 'M', 'M', 'M', 'B', 'B', 'B', 'B', 'B', 'B', 'M',\n",
       "       'B', 'M', 'B', 'B', 'M', 'B', 'B', 'M', 'B', 'M', 'M', 'B', 'B',\n",
       "       'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',\n",
       "       'B', 'M', 'B', 'M', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',\n",
       "       'B', 'B', 'B', 'B', 'B', 'M', 'B', 'B', 'B', 'M', 'B', 'M', 'B',\n",
       "       'B', 'B', 'B', 'M', 'M', 'M', 'B', 'B', 'B', 'B', 'M', 'B', 'M',\n",
       "       'B', 'M', 'M', 'B', 'B', 'M', 'B', 'B', 'B', 'M', 'B', 'B', 'B',\n",
       "       'M', 'M', 'M', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'M',\n",
       "       'B', 'M', 'M', 'B', 'M', 'M', 'M', 'B', 'M', 'M', 'B', 'B', 'B',\n",
       "       'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'M',\n",
       "       'B', 'B', 'M', 'M', 'B', 'B', 'B', 'B', 'B', 'B', 'M', 'B', 'B',\n",
       "       'B', 'B', 'B', 'M', 'B', 'M', 'B', 'B', 'B', 'B', 'B', 'M', 'B',\n",
       "       'B', 'M', 'B', 'B', 'B', 'M', 'B', 'B', 'B', 'B', 'B', 'B', 'B',\n",
       "       'B', 'M', 'B', 'M', 'M', 'B', 'M', 'B', 'B', 'B', 'B', 'B', 'M',\n",
       "       'B', 'B', 'M', 'B', 'M', 'B', 'B', 'M', 'B', 'M', 'B', 'B', 'B',\n",
       "       'B', 'B', 'B', 'B', 'B', 'M', 'M', 'B', 'B', 'B', 'M', 'B', 'B',\n",
       "       'M', 'B', 'B', 'B', 'M', 'B', 'B', 'B', 'M', 'B', 'B', 'M', 'B',\n",
       "       'B', 'B', 'B', 'B', 'B', 'B', 'M', 'B', 'M', 'B', 'M', 'M', 'B',\n",
       "       'B', 'B', 'B', 'B', 'M', 'M', 'B', 'B', 'B', 'M', 'B', 'B', 'B',\n",
       "       'B', 'B', 'M', 'B', 'B', 'M', 'B', 'M', 'B', 'M', 'M', 'B', 'B',\n",
       "       'B', 'M', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',\n",
       "       'M', 'B', 'M', 'B', 'B', 'B', 'B', 'B', 'M', 'B', 'B', 'B', 'B',\n",
       "       'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B',\n",
       "       'B', 'B', 'B', 'M', 'M', 'M', 'M', 'M', 'M', 'B'], dtype=object)"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "target_predict = model.predict(features_train)\n",
    "target_predict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "1780595c-546f-438f-8f76-bdc597a88f64",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "8b842b42-9559-4221-9c98-eb20c1a6852d",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9244288224956063"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "##0.9244288224956063\n",
    "accuracy_score(target_train,target_predict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "560ec84a-2048-43a1-b5b8-0f7d9fd850e7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
