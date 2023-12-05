import xlwt
from repository.bamboohr_repository import BamboohrRepository
from validation.google_workspace_validation import GoogleWorkspaceValidation
from validation.slack_validation import SlackValidation
from validation.atlassian_validation import AtlassianValidation
from service.upload_to_google_drive import GoogleDriveUpload
from service.upload_to_google_sheets import GoogleSheetsUpload

SAMPLE_SPREADSHEETS_IDS = [
    '1UFXCGOn80TiRhYFUbzE7x6l3ANJmPXc_51CC5DOuQEM',
    '1re8gSevsb2HqipZYwM87yO4XQ54iAB5OQM6ubFKBpkE' 
]

SAMPLE_RANGE_NAME = 'Employee Profile Validation!A3:E500'

class UpdateInformation:

    def __init__(self, credentials):
        self.credentials = credentials

    def update_info_all_employees(self):
        book = xlwt.Workbook()
        bamboo_emails = BamboohrRepository.upload_bamboo_emails(BamboohrRepository.get_employees_bamboo_data())
        bamboo_first_names_and_last_names=BamboohrRepository.upload_bamboo_first_names_and_last_names(BamboohrRepository.get_employees_bamboo_data())
        google_workspace_validation_list=GoogleWorkspaceValidation(credentials=self.credentials).upload_validation_list()
        slack_validation_list=SlackValidation.upload_validation_list()
        atlassian_validation_list=AtlassianValidation.upload_validation_list()

        GoogleDriveUpload(
            credentials=self.credentials,
            book=book,
            bamboo_emails=bamboo_emails,
            bamboo_first_names_and_last_names=bamboo_first_names_and_last_names,
            google_workspace_validation_list=google_workspace_validation_list,
            slack_validation_list=slack_validation_list,
            atlassian_validation_list=atlassian_validation_list
        ).upload_to_folder(folder_id='1Lfa-v8YTISfOomL_4CxHgR4q0zfenTXk')

        GoogleSheetsUpload(
            credentials=self.credentials,
            spreadsheets_ids=SAMPLE_SPREADSHEETS_IDS,
            range_name=SAMPLE_RANGE_NAME,
            bamboo_emails=bamboo_emails,
            bamboo_first_names_and_last_names=bamboo_first_names_and_last_names,
            google_workspace_validation_list=google_workspace_validation_list,
            slack_validation_list=slack_validation_list,
            atlassian_validation_list=atlassian_validation_list
        ).upload_to_list()