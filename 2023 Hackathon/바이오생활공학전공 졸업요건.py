def check_bio_major(df, track_type):
    jeongi = 0   # 전기
    jepil = 0    # 전필
    jeseon = 0   # 전선
    advanced = 0 # 3~4000 단위

    # Check for each category
    for i in range(len(df)):
        category = str(df.loc[i, 'category'])
        credit = df.loc[i, 'credits']

        # 전공 분류
        if category == '전기':
            jeongi += credit
        elif category == '전필':
            jepil += credit
        elif category == '전선':
            jeseon += credit

        # 3000 / 4000 단위 확인
        course_name = str(df.loc[i, 'course_name'])
        if '3000' in course_name or '4000' in course_name:
            advanced += credit

    # -----------------------------
    # Standard Credits
    if track_type == "단일전공":
        req_jeongi = 18
        req_jepil = 12
        req_jeseon = 24
        req_advanced = 45

    elif track_type == "복수전공1":
        req_jeongi = 9
        req_jepil = 12
        req_jeseon = 15
        req_advanced = 45   # ⭐ 여기 응용정보학과랑 다른 포인트

    elif track_type == "복수전공2":
        req_jeongi = 9
        req_jepil = 12
        req_jeseon = 15
        req_advanced = None

    else:  # 부전공
        req_jeongi = 6
        req_jepil = 6
        req_jeseon = 9
        req_advanced = None

    # -----------------------------
    # Check Missing Credits
    missing = []

    if jeongi < req_jeongi:
        missing.append(f"전기 {req_jeongi - jeongi}학점 부족")

    if jepil < req_jepil:
        missing.append(f"전필 {req_jepil - jepil}학점 부족")

    if jeseon < req_jeseon:
        missing.append(f"전선 {req_jeseon - jeseon}학점 부족")

    # Check only for 단일전공만 (3~4000)
    if req_advanced is not None:
        if advanced < req_advanced:
            missing.append(f"3~4000단위 {req_advanced - advanced}학점 부족")

    # -----------------------------
    # Result
    if len(missing) == 0:
        return "바이오생활공학전공 요건을 모두 충족했습니다!"
    else:
        result = "바이오생활공학전공 요건 부족:\n"
        for item in missing:
            result += "- " + item + "\n"
        return result
