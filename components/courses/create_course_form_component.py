from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.input import Input
from elements.textarea import TextArea

class CreateCourseFormComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)
        self.title_input = Input(page,'create-course-form-title-input', 'Title Input')
        self.estimate_input = Input(page,'create-course-form-estimated-time-input', 'Estimated Input')
        self.description_input = TextArea(
            page,'create-course-form-description-input', 'Description Textarea'
        )
        self.max_score_input = Input(page,'create-course-form-max-score-input', 'Max Score Input')
        self.min_score_input = Input(page,'create-course-form-min-score-input', 'Min Score Input')


    def fill(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str,
    ):
        self.title_input.fill(title)
        self.title_input.check_value(title)

        self.estimate_input.fill(estimated_time)
        self.estimate_input.check_value(estimated_time)

        self.description_input.fill(description)
        self.description_input.check_value(description)

        self.max_score_input.fill(max_score)
        self.max_score_input.check_value(max_score)

        self.min_score_input.fill(min_score)
        self.min_score_input.check_value(min_score)

    def check_visible(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str,
    ):
        self.title_input.check_visible()
        self.title_input.check_value(title)

        self.estimate_input.check_visible()
        self.estimate_input.check_value(estimated_time)

        self.description_input.check_visible()
        self.description_input.check_value(description)

        self.max_score_input.check_visible()
        self.max_score_input.check_value(max_score)

        self.min_score_input.check_visible()
        self.min_score_input.check_value(min_score)
