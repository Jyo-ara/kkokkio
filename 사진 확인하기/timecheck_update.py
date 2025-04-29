import os
from datetime import datetime, timedelta
from collections import defaultdict

folder_path = r"C:\Users\Admin\Desktop\꼬끼오\검사\0428"

summary_list = []  # 🔹 전체 특이사항 요약용 리스트

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'r') as f:
            lines = f.readlines()

        timestamps = []
        for line in lines:
            line = line.strip().strip('"')
            name = os.path.basename(line).replace(".jpg", "")
            try:
                dt = datetime.strptime(name, "%Y_%m_%d_%H_%M_%S")
                timestamps.append(dt)
            except ValueError:
                print(f"[{filename}] 잘못된 형식: {name}")

        if not timestamps:
            print(f"\n📄 {filename} - 유효한 타임스탬프 없음")
            continue

        timestamps.sort()
        start_time = timestamps[0]
        end_time = timestamps[-1]

        start_min = start_time.replace(second=0)
        end_min = end_time.replace(second=0)

        total_minutes = int((end_min - start_min).total_seconds() // 60) + 1
        hours = total_minutes // 60
        minutes = total_minutes % 60

        minute_counts = defaultdict(int)
        for t in timestamps:
            minute_key = t.replace(second=0)
            minute_counts[minute_key] += 1

        missing_minutes = []
        partially_saved_minutes = []
        expected_time = start_min

        while expected_time <= end_min:
            count = minute_counts.get(expected_time, 0)
            if count != 2:
                missing_minutes.append(expected_time)
                if count == 1:
                    partially_saved_minutes.append(expected_time)
            expected_time += timedelta(minutes=1)

        # 출력
        print(f"\n📄 파일 : {filename}")
        print(f"  - 시작 시간 : {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  - 끝 시간 : {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  - 총 시간 : {total_minutes}분 ({hours}시간 {minutes}분)")
        print(f"  - 총 이미지 수 : {len(timestamps)}")
        print(f"  - 누락된 시간 : {len(missing_minutes)}")

        # 특이사항: 누락 구간 그룹핑 및 요약
        if missing_minutes:
            print(f"  - ⚠️ 특이사항")
            group_start = missing_minutes[0]
            prev = group_start
            group_minutes = [group_start]

            folder_name = os.path.basename(filename).split('.')[0].zfill(2)

            for curr in missing_minutes[1:] + [None]:
                if curr is None or (curr - prev).total_seconds() > 60:
                    group_end = prev
                    duration = int((group_end - group_start).total_seconds() // 60) + 1

                    # 해당 구간 안에 1장 저장된 시간 필터링
                    partials_in_group = [
                        m.strftime('%H:%M') for m in partially_saved_minutes
                        if group_start <= m <= group_end
                    ]
                    if partials_in_group:
                        partial_info = f" ({', '.join(partials_in_group)} 에 1장씩 저장됨)"
                    else:
                        partial_info = ""

                    # 개별 파일 출력
                    print(f"    {folder_name}번 폴더 {group_start.strftime('%Y-%m-%d %H:%M')} ~ {group_end.strftime('%Y-%m-%d %H:%M')} 사이 {duration}개 누락{partial_info}")

                    # 전체 요약 리스트에 추가
                    summary_list.append(
                        f"{folder_name}번 폴더 {group_start.strftime('%Y-%m-%d %H:%M')} ~ {group_end.strftime('%Y-%m-%d %H:%M')} 사이 {duration}개 누락{partial_info}"
                    )

                    # 다음 그룹 초기화
                    group_start = curr
                    group_minutes = [curr] if curr else []
                else:
                    group_minutes.append(curr)
                prev = curr

# 🔻 마지막 전체 특이사항 요약
if summary_list:
    print("\n📌 전체 특이사항 요약:")
    for item in summary_list:
        print(item)
