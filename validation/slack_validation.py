from repository.bamboohr_repository import BamboohrRepository
from repository.slack_repository import SlackRepository

class SlackValidation:

    def upload_validation_list(employee) -> list: 
        list_for_upload = list()
        employees_from_bamboohr = BamboohrRepository.get_employees_bamboo_data()
        employees_from_slack = SlackRepository.get_employees_slack_data()  
        
        if employee in employees_from_bamboohr: 
            
            if list(employees_from_slack.keys()).count(employee) > 0:   
                status = ['✕', '✕', '✕', '✕', '✕', '✕'] 
                # Если реальное имя в Slack соответствуют стандарту!
                if employees_from_slack[employee][0] != employees_from_bamboohr[employee][0]: 
                    status[0] = '✓' 
                # Если отображаемое имя в Slack соответствуют стандарту!
                if employees_from_slack[employee][1] != employees_from_bamboohr[employee][0]: 
                    status[1] = '✓' 
                # Если есть описание(должность, откуда человек)!
                if employees_from_slack[employee][2] != '':  
                    status[2] = '✓' 
                # Если описание(должность, откуда человек) задано по стандарту!
                if len(employees_from_slack[employee][2].split(', ')) == 3:
                    status[3] = '✓' 
                    # Если задана актуальная локация!
                    if (
                        employees_from_bamboohr[employee][1] == employees_from_slack[employee][2].split(', ')[1] and
                        employees_from_bamboohr[employee][2] == employees_from_slack[employee][2].split(', ')[2]
                    ): 
                        status[4] = '✓'
                # Если задан номер телефона!
                if employees_from_slack[employee][3] != '': 
                    status[5] = '✓'
                if len(status) == 0:
                    status.append("Success!")
                status_to_string = "" 
                list_for_upload.append(status_to_string.join(status)) 
            
            else:
                
                list_for_upload.append("Not Found")
        
        return list_for_upload


