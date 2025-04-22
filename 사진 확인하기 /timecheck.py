import os
from datetime import datetime, timedelta
from collections import defaultdict

# 분석할 폴더 경로 설정 (예: ./0421 또는 절대 경로)
folder_path = r"C:\Users\Admin\Desktop\꼬끼오\검사\0421"  # ← 여기에 경로 바꿔주세요

# 폴더 내 모든 .txt 파일 반복
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

        # 시간 정렬
        timestamps.sort()
        start_time = timestamps[0]  # 초 포함
        end_time = timestamps[-1]  # 초 포함

        # 분 단위로 맞춘 시간 (내부 계산용)
        start_min = start_time.replace(second=0)
        end_min = end_time.replace(second=0)

        # 총 시간 계산
        total_minutes = int((end_min - start_min).total_seconds() // 60) + 1
        hours = total_minutes // 60
        minutes = total_minutes % 60

        # 분 단위 카운트
        minute_counts = defaultdict(int)
        for t in timestamps:
            minute_key = t.replace(second=0)
            minute_counts[minute_key] += 1

        # 누락 및 잘못된 저장 탐지
        missing_minutes = []
        wrong_count_minutes = []
        expected_time = start_min

        while expected_time <= end_min:
            count = minute_counts.get(expected_time, 0)
            if count != 2:
                if count == 0:
                    missing_minutes.append(expected_time)
                else:
                    wrong_count_minutes.append((expected_time, count))
            expected_time += timedelta(minutes=1)

        # 결과 출력
        print(f"\n📄 파일 : {filename}")
        print(f"  - 시작 시간 : {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  - 끝 시간 : {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  - 총 시간 : {total_minutes}분 ({hours}시간 {minutes}분)")
        print(f"  - 총 이미지 수 : {len(timestamps)}")
        print(f"  - 누락된 시간 : {len(missing_minutes)}")
        print(f"  - 저장 개수 오류 시간 : {len(wrong_count_minutes)}")

        if missing_minutes:
            print("    ⛔ 누락된 시간:")
            for m in missing_minutes:
                print(f"      - {m.strftime('%Y-%m-%d %H:%M')}")

        if wrong_count_minutes:
            print("    ⚠️ 저장 개수가 다른 시간:")
            for m, c in wrong_count_minutes:
                print(f"      - {m.strftime('%Y-%m-%d %H:%M')}: {c}장 저장됨")
