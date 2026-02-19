def check_glc_requirements(df, english_exemption):
    chapel = 0                      #채플
    christian = 0                   #기독교이해
    glc_english = 0                 #영어
    liberal = 0                     #대학교양
    rc = 0                          #RC

    # checking credit for each category 
    for i in range(len(df)):
        name = str(df.loc[i, 'course_name'])
        credit = df.loc[i, 'credits']

        if '채플' in name:
            chapel += credit
        elif '기독교의 이해' in name:
            christian += credit
        elif 'GLC 영어' in name:
            glc_english += credit
        elif 'RC 101' in name:
            rc += credit
        else:
            liberal += credit

    # -----------------------------
    # Standard Requirements 
    if english_exemption == 0:
        required_basic = 11
        required_glc = 6
    elif english_exemption == 1:
        required_basic = 8
        required_glc = 3
    else:
        required_basic = 5
        required_glc = 0

    required_chapel = 2
    required_christian = 3
    required_liberal = 9
    required_rc = 1

    # -----------------------------
    # Finding Missing Credits Needed
    missing = []

    if chapel < required_chapel:
        missing.append(f"채플 {required_chapel - chapel}학점 부족")

    if christian < required_christian:
        missing.append(f"기독교의 이해 {required_christian - christian}학점 부족")

    if glc_english < required_glc:
        missing.append(f"GLC 영어 {required_glc - glc_english}학점 부족")

    if liberal < required_liberal:
        missing.append(f"대학교양 {required_liberal - liberal}학점 부족")

    if rc < required_rc:
        missing.append(f"RC {required_rc - rc}학점 부족")

    # -----------------------------
    # Result
    if len(missing) == 0:
        return "모든 교양 이수 요건을 충족했습니다!"
    else:
        result = "아직 부족한 부분:\n"
        for item in missing:
            result += "- " + item + "\n"
        return result
