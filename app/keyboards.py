from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)

import database.requests as bd

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="✖️Отмена")]],
    resize_keyboard=True,
    input_field_placeholder="Choose the button",
)

geo_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📍Отправить местоположение", request_location=True)],
        [KeyboardButton(text="✖️Отмена")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Send your geolocation",
)


first_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Авторизоваться"), KeyboardButton(text="Отметиться")],
        [KeyboardButton(text="Информация"), KeyboardButton(text="Расписание")],
        [KeyboardButton(text="Списки присутствующих")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose the button",
)


def get_education_kb():
    buttons = [[InlineKeyboardButton(text="✖️Отмена", callback_data="undo")]]
    buttons_buf = [
        [InlineKeyboardButton(text="Бакалавриат", callback_data="education_бакалавр")],
        [InlineKeyboardButton(text="Магистратура", callback_data="education_магистр")],
    ]

    buttons.extend(buttons_buf)
    education_kb = InlineKeyboardMarkup(row_width=3, inline_keyboard=buttons)
    return education_kb


def get_institute_kb(education, page):
    institutes = bd.get_institute(education)
    pages = len(institutes) // 7
    if not len(institutes) % 7 == 0:
        pages += 1
    buttons = [
        [InlineKeyboardButton(text="✖️ Отмена", callback_data="undo")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_education")],
    ]
    buttons_buf = [
        [
            InlineKeyboardButton(
                text=el["Institute"],
                callback_data="id_institute_" + str(el["id_institute"]),
            )
        ]
        for el in institutes
    ]
    start_index = (page - 1) * 7
    end_index = page * 7
    if len(institutes) < end_index:
        end_index = len(institutes)
    institute_for_page = buttons_buf[start_index:end_index]

    end_buttons = []
    if page > 1:
        end_buttons.append(
            InlineKeyboardButton(
                text="⬅️", callback_data="institute_page_" + str(page - 1)
            )
        )

    if page < pages:
        end_buttons.append(
            InlineKeyboardButton(
                text="➡️", callback_data="institute_page_" + str(page + 1)
            )
        )

    buttons.extend(institute_for_page)
    buttons.extend([end_buttons])
    institutes_kb = InlineKeyboardMarkup(row_width=3, inline_keyboard=buttons)
    return institutes_kb


def get_fuclty_kb(institute, education, page):
    fuclty = bd.get_fuclty(institute, education)
    pages = len(fuclty) // 7
    if not len(fuclty) % 7 == 0:
        pages += 1
    buttons = [InlineKeyboardButton(text="✖️ Отмена", callback_data="undo")]
    button_back = [
        InlineKeyboardButton(text="🔙 Назад", callback_data="education_back")
    ]

    group_buttons = [
        [
            InlineKeyboardButton(
                text=el["Fuclty"], callback_data="id_fuclty_" + str(el["id_fuclty"])
            )
        ]
        for el in fuclty
    ]
    start_index = (page - 1) * 7
    end_index = page * 7
    if len(fuclty) < end_index:
        end_index = len(fuclty)
    fuclty_for_page = group_buttons[start_index:end_index]

    end_buttons = []
    if page > 1:
        end_buttons.append(
            InlineKeyboardButton(text="⬅️", callback_data="fuclty_page_" + str(page - 1))
        )

    if page < pages:
        end_buttons.append(
            InlineKeyboardButton(text="➡️", callback_data="fuclty_page_" + str(page + 1))
        )

    result_button = [buttons, button_back] + fuclty_for_page
    result_button.extend([end_buttons])
    fuclty_kb = InlineKeyboardMarkup(row_width=3, inline_keyboard=result_button)
    return fuclty_kb


def get_group_kb(institute, course, education, page):
    group = bd.get_groups(institute, course, education)
    buttons = []
    if course > 1:
        buttons.append(
            InlineKeyboardButton(
                text=str(course - 1) + " курс",
                callback_data="course_" + str(course - 1),
            )
        )

    buttons.append(InlineKeyboardButton(text="✖️ Отмена", callback_data="undo"))

    if course < 4:
        buttons.append(
            InlineKeyboardButton(
                text=str(course + 1) + " курс",
                callback_data="course_" + str(course + 1),
            )
        )

    button_back = [
        InlineKeyboardButton(text="🔙 Назад", callback_data="id_institute_back")
    ]
    group_buttons = [
        InlineKeyboardButton(
            text=el["Study_group"],
            callback_data="id_study_group_" + str(el["id_study_group"]),
        )
        for el in group
    ]
    group_buttons_pairs = [
        list(pair) for pair in zip(group_buttons[::2], group_buttons[1::2])
    ]
    pages = len(group_buttons_pairs) // 7
    if not len(group_buttons_pairs) % 7 == 0:
        pages += 1
    start_index = (page - 1) * 7
    end_index = page * 7
    if len(group_buttons_pairs) < end_index:
        end_index = len(group_buttons_pairs)

    end_buttons = []
    if page > 1:
        end_buttons.append(
            InlineKeyboardButton(
                text="⬅️",
                callback_data="study_group_page_" + str(page - 1) + "_" + str(course),
            )
        )

    if page < pages:
        end_buttons.append(
            InlineKeyboardButton(
                text="➡️",
                callback_data="study_group_page_" + str(page + 1) + "_" + str(course),
            )
        )

    group_for_page = group_buttons_pairs[start_index:end_index]
    result_button = [buttons] + [button_back]
    result_button += group_for_page
    result_button.extend([end_buttons])
    groups_kb = InlineKeyboardMarkup(row_width=3, inline_keyboard=result_button)
    return groups_kb


def get_student_kb(group, page):
    student = bd.get_student(group)
    buttons = [
        [InlineKeyboardButton(text="✖️ Отмена", callback_data="undo")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="id_fuclty_back")],
    ]

    group_buttons = [
        [
            InlineKeyboardButton(
                text=el["Student"], callback_data="id_student_" + str(el["id_student"])
            )
        ]
        for el in student
    ]

    pages = len(student) // 7
    if not len(student) % 7 == 0:
        pages += 1
    start_index = (page - 1) * 7
    end_index = page * 7
    if len(student) < end_index:
        end_index = len(student)

    end_buttons = []
    if page > 1:
        end_buttons.append(
            InlineKeyboardButton(
                text="⬅️", callback_data="student_page_" + str(page - 1)
            )
        )

    if page < pages:
        end_buttons.append(
            InlineKeyboardButton(
                text="➡️", callback_data="student_page_" + str(page + 1)
            )
        )

    group_for_page = group_buttons[start_index:end_index]
    result_button = buttons + group_for_page
    result_button.extend([end_buttons])
    student_kb = InlineKeyboardMarkup(row_width=3, inline_keyboard=result_button)
    return student_kb
