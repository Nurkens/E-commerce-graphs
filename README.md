# 📊 Olist E-commerce Project (Assignment 2)

Проект основан на **бразильском e-commerce датасете Olist**.
Задача: загрузить данные в PostgreSQL, выполнить SQL-анализ, построить визуализации и экспортировать результаты в Excel.

---

## 🚀 Основные возможности

- 📥 Импорт 9 CSV-файлов в PostgreSQL с автоматическим созданием таблиц.
- 🔗 Работа с данными через SQL (`JOIN`, `GROUP BY`, `ORDER BY`, агрегатные функции).
- 📊 Визуализации с использованием **matplotlib** и **Plotly**:

  - Pie chart — распределение заказов по штатам.
  - Bar chart — топ-20 городов по количеству заказов.
  - Horizontal bar — средняя задержка доставки по регионам.
  - Line chart — динамика заказов по времени.
  - Histogram — распределение числа заказов на одного клиента.
  - Scatter plot — зависимость заказов и среднего рейтинга отзывов.
  - Plotly slider — интерактивный график заказов по месяцам.

- 📑 Экспорт в Excel с:

  - автофильтрами,
  - замороженной верхней строкой,
  - условным форматированием (градиент цветов).

---

## 📂 Структура проекта

```
E-commerce_Olist/
├── datasets/              # CSV-файлы Olist
├── charts/                # Графики (PNG + HTML)
├── exports/               # Excel-отчёты
├── config.py              # Конфигурация подключения к PostgreSQL
├── db_create.py           # Скрипт для инициализации БД (при необходимости)
├── data_import.py         # Импорт CSV в PostgreSQL
├── analytics.py           # SQL + визуализации + экспорт в Excel
├── queries.sql            # Сохранённые SQL-запросы
├── requirements.txt       # Зависимости Python
└── README.md
```

---

## ⚙️ Как запустить

1. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

2. Настроить переменные окружения или `config.py` (PostgreSQL user, password, port, dbname).
3. Очистить схему (один раз перед загрузкой):

   ```sql
   DROP SCHEMA public CASCADE;
   CREATE SCHEMA public;
   ```

4. Импортировать данные:

   ```bash
   python data_import.py
   ```

5. Построить графики и отчёт:

   ```bash
   python analytics.py
   ```

---

## 📊 Результаты

- Папка **charts/**:

  - `pie.png`
  - `bar.png`
  - `hbar.png`
  - `line.png`
  - `hist.png`
  - `scatter.png`
  - `plotly_slider.html` (открывается в браузере)

- Папка **exports/**:

  - `report.xlsx` (Excel с листами `customers`, `orders` и форматированием)
