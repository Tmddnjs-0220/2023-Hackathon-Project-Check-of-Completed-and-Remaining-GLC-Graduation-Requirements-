def check_international_trade_major(df, track_type):
    jeongi = 0   # 전기
    jeseon = 0   # 전선
    advanced = 0 # 3~4000 단위
    total_major = 0  # 총 전공학점

    # -----------------------------
    # Check for each category
    for i in range(len(df)):
        category = str(df.loc[i, 'category'])
        credit = df.loc[i, 'credits']

        # 전공 분류
        if category == '전기':
            jeongi += credit
            total_major += credit
        elif category == '전선':
            jeseon += credit
            total_major += credit

        # 3000 / 4000 단위 확인
        course_name = str(df.loc[i, 'course_name'])
        if '3000' in course_name or '4000' in course_name:
            advanced += credit

    # -----------------------------
    # Standard Credits
    if track_type == "단일전공 이수":
        req_jeongi = 9
        req_jeseon = 39
        required_total = 48
        req_advanced = 45

    elif track_type == "캠퍼스내 복수전공 1전공":
        req_jeongi = 6
        req_jeseon = 30
        required_total = 36
        req_advanced = 45

    elif track_type == "캠퍼스내 복수전공 2전공":
        req_jeongi = 6
        req_jeseon = 30
        required_total = 36
        req_advanced = None

    else:
        return "올바른 전공 유형을 입력하세요."

    # -----------------------------
    # Check Missing Credits
    missing = []

    if jeongi < req_jeongi:
        missing.append(f"전기 {req_jeongi - jeongi}학점 부족")

    if jeseon < req_jeseon:
        missing.append(f"전선 {req_jeseon - jeseon}학점 부족")

    # 총 전공학점 체크 (단일전공만 48 정확히 요구)
    if track_type == "단일전공 이수":
        if total_major < required_total:
            missing.append(f"총 전공학점 {required_total - total_major}학점 부족")
        elif total_major > required_total:
            missing.append(f"총 전공학점 {total_major - required_total}학점 초과")
    else:
        if total_major < required_total:
            missing.append(f"총 전공학점 {required_total - total_major}학점 부족")

    # 3~4000단위 체크 (None 아닌 경우만)
    if req_advanced is not None:
        if advanced < req_advanced:
            missing.append(f"3~4000단위 {req_advanced - advanced}학점 부족")

    # -----------------------------
    # Result
    if len(missing) == 0:
        return "국제통상전공 요건을 모두 충족했습니다!"
    else:
        result = "국제통상전공 요건 부족:\n"
        for item in missing:
            result += "- " + item + "\n"
        return result