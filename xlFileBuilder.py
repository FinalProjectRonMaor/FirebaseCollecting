import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd

cred = credentials.Certificate("serviceAccountKey.json")  # replace with the path to your credentials file
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://emotiondetectorapidata-default-rtdb.firebaseio.com/'
})
ref = db.reference()

# get the data from Firebase
data = []
maxLenTaps = 0
maxLenDrags = 0
numberOfValidMobileEntries = 0

print('Collecting data from Firebase DB')
for recordVersion in ref.get().keys():
    records = ref.child(recordVersion).get();
    if (recordVersion == 'recordsV2'):
        for i, user_id in enumerate(ref.child(recordVersion).get().keys()):
            user_data = records[user_id];
            if (user_data['isMobile'] == False or user_data['typeKeyBoardTimeArray'][1] == 0):
                continue
            numberOfValidMobileEntries += 1
            dataDict = {}
            print('User-' + str(i))
            # if(recordVersion == 'recordsV1'):
            #     dict_data = buildV1recordsUserDataDict(user_data)
            #     data.append(dict_data)
            # screen_dim = user_data['ScreenDimensions']
            avg_pixel = user_data['avgPixelPerSecond']
            motoric_prob = user_data['form']['motoricProblem']
            motoric_info = user_data['form']['motoricProblemInfo']
            native_lang = user_data['form']['nativeLanguage']
            textarea = user_data['form']['textarea']
            dominant_hand = user_data['form']['dominantHand']
            user_age = user_data['form']['userAge']
            user_sex = user_data['form']['userSex']
            is_mobile = user_data['isMobile']
            fear_level = user_data['form']['fearLevel']
            joy_level = user_data['form']['joyLevel']
            sadness_level = user_data['form']['sadnessLevel']
            distructed_level = user_data['form']['distructedLevel']
            stress_level = user_data['form']['stressLevel']
            tired_level = user_data['form']['tiredLevel']
            mouse_click_matrix = user_data['mouseClickMatrix']
            mouse_click_time_array = user_data['mouseClickTimeArray']
            mouse_move_matrix = user_data['mouseMoveMatrix']
            mouse_move_time_array = user_data['mouseMoveTimeArray']
            scrollTimeArray = user_data['scrollTimeArray']
            touchSlideTimeArray = user_data['touchSlideTimeArray']
            type_keyboard_key_array = user_data['typeKeyBoardKeyArray']
            type_keyboard_time_array = user_data['typeKeyBoardTimeArray']
            if (len(mouse_click_time_array) > maxLenTaps):
                maxLenTaps = len(mouse_click_time_array)
            if (len(mouse_move_time_array) > maxLenDrags):
                maxLenDrags = len(mouse_move_time_array)
            backCount = 0
            if (user_sex == 'male'):
                user_sex = 0
            else:
                user_sex = 1
            if (dominant_hand == 'right'):
                dominant_hand = 0
            else:
                dominant_hand = 1
            if (motoric_prob == 'n'):
                motoric_prob = 0
            else:
                motoric_prob = 1
            for back in type_keyboard_key_array:
                if back == 'Backspace':
                    backCount = backCount + 1
            backCount = backCount / len(type_keyboard_key_array)
            dataDict = {"User's Age": user_age,
                        "User's Sex": user_sex,
                        "Speed": avg_pixel,
                        "Dominant Hand":dominant_hand,
                        "Backspaces Count":backCount,
                        "Joy Level":joy_level,
                        "Sadness Level":sadness_level,
                        "Stress Level":stress_level,
                        "Tired Level":tired_level,
                        "Fear Level":fear_level,
                        "Distructed Level":distructed_level}
            data.append(dataDict)
    if (recordVersion == 'recordsV3'):
        for i, user_id in enumerate(ref.child(recordVersion).get().keys()):
            user_data = records[user_id];
            numberOfValidMobileEntries += 1
            dataDict = {}
            print('User-' + str(i))
            # if(recordVersion == 'recordsV1'):
            #     dict_data = buildV1recordsUserDataDict(user_data)
            #     data.append(dict_data)
            # screen_dim = user_data['ScreenDimensions']
            avg_pixel = user_data['avgPixelPerSecond']
            motoric_prob = user_data['form']['motoricProblem']
            motoric_info = user_data['form']['motoricProblemInfo']
            native_lang = user_data['form']['nativeLanguage']
            textarea = user_data['form']['textarea']
            dominant_hand = user_data['form']['dominantHand']
            user_age = user_data['form']['userAge']
            user_sex = user_data['form']['userSex']
            is_mobile = user_data['isMobile']
            fear_level = user_data['form']['fearLevel']
            joy_level = user_data['form']['joyLevel']
            sadness_level = user_data['form']['sadnessLevel']
            distructed_level = user_data['form']['distructedLevel']
            stress_level = user_data['form']['stressLevel']
            tired_level = user_data['form']['tiredLevel']
            mouse_click_matrix = user_data['mouseClickMatrix']
            mouse_click_time_array = user_data['mouseClickTimeArray']
            mouse_move_matrix = user_data['mouseMoveMatrix']
            mouse_move_time_array = user_data['mouseMoveTimeArray']
            scrollTimeArray = user_data['scrollTimeArray']
            touchSlideTimeArray = user_data['touchSlideTimeArray']
            type_keyboard_key_array = user_data['typeKeyBoardKeyArray']
            type_keyboard_time_array = user_data['typeKeyBoardTimeArray']
            if (len(mouse_click_time_array) > maxLenTaps):
                maxLenTaps = len(mouse_click_time_array)
            if (len(mouse_move_time_array) > maxLenDrags):
                maxLenDrags = len(mouse_move_time_array)
            backCount = 0
            if (user_sex == 'male'):
                user_sex = 0
            else:
                user_sex = 1
            if (dominant_hand == 'right'):
                dominant_hand = 0
            else:
                dominant_hand = 1
            if (motoric_prob == 'n'):
                motoric_prob = 0
            else:
                motoric_prob = 1
            for back in type_keyboard_key_array:
                if back == 'Backspace':
                    backCount = backCount + 1
            backCount = backCount / len(type_keyboard_key_array)
            dataDict = {"User's Age": user_age,
                        "User's Sex": user_sex,
                        "Speed": avg_pixel,
                        "Dominant Hand":dominant_hand,
                        "Backspaces Count":backCount,
                        "Joy Level":joy_level,
                        "Sadness Level":sadness_level,
                        "Stress Level":stress_level,
                        "Tired Level":tired_level,
                        "Fear Level":fear_level,
                        "Distructed Level":distructed_level}
            data.append(dataDict)

def create_excel_file(data, filename):
    # Convert the array of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Create a writer object for the Excel file
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')

    # Write the DataFrame to the Excel file
    df.to_excel(writer, index=False)

    # Save the Excel file
    writer.save()

filename = 'data.xlsx'
create_excel_file(data, filename)