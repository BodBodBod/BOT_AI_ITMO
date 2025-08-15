from parser.parser_utils import get_page, save_json
from config import PROGRAM_AI_PRODUCT_URL

def parse_ai_product():
    """
    Парсит страницу программы "AI и управление продуктом"
    """
    soup = get_page(PROGRAM_AI_PRODUCT_URL)
    if not soup:
        return None

    data = {"program": "AI и управление продуктом", "semesters": []}

    # Ищем таблицы с учебным планом (по классу или структуре)
    tables = soup.find_all("table", {"class": "curriculum-table"})
    for i, table in enumerate(tables[:4]):  # Предполагаем 4 семестра
        semester_data = {"number": i + 1, "courses": []}
        rows = table.find_all("tr")[1:]  # Пропускаем заголовок
        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 3:
                course = {
                    "name": cols[0].get_text(strip=True),
                    "type": "required" if "обязатель" in cols[1].get_text().lower() else "elective",
                    "credits": cols[2].get_text(strip=True),
                    "description": cols[3].get_text(strip=True) if len(cols) > 3 else ""
                }
                semester_data["courses"].append(course)
        data["semesters"].append(semester_data)

    save_json(data, "ai_product_curriculum.json")
    return data