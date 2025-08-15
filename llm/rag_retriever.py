import json
import os
from config import DATA_DIR


def load_curriculum(program_name):
    """
    Загружает учебный план по имени программы.
    Возвращает словарь или None, если файл не найден.
    """
    path = os.path.join(DATA_DIR, f"{program_name}_curriculum.json")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


def find_relevant_context(query: str) -> str:
    """
    Находит релевантные данные из учебных планов на основе запроса.
    Возвращает текст контекста для LLM.
    """
    query_lower = query.lower()
    context_parts = []

    # Проверяем, содержит ли запрос "AI" (без "product")
    if any(keyword in query_lower for keyword in ["ai", "искусственный интеллект", "мл", "machine learning"]):
        ai_data = load_curriculum("ai")
        if ai_data:
            context_parts.append("Программа: Искусственный интеллект (AI)")
            for semester in ai_data["semesters"]:
                context_parts.append(f"Семестр {semester['number']}:")
                for course in semester["courses"]:
                    type_label = "по выбору" if course["type"] == "elective" else "обязательный"
                    context_parts.append(f"  - {course['name']} ({type_label}, {course['credits']} ECTS)")

    # Проверяем, содержит ли запрос "AI & Product" или "управление продуктом"
    if any(keyword in query_lower for keyword in ["ai product", "управление продуктом", "product", "продукт"]):
        ai_product_data = load_curriculum("ai_product")
        if ai_product_data:
            context_parts.append("Программа: AI и управление продуктом")
            for semester in ai_product_data["semesters"]:
                context_parts.append(f"Семестр {semester['number']}:")
                for course in semester["courses"]:
                    type_label = "по выбору" if course["type"] == "elective" else "обязательный"
                    context_parts.append(f"  - {course['name']} ({type_label}, {course['credits']} ECTS)")

    # Если ничего не найдено — возвращаем пустой контекст
    if not context_parts:
        return ""

    return "\n".join(context_parts)