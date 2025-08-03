from django.core.management.base import BaseCommand
from norsklaer_backend.apps.lessons.models import Lesson, Quiz

class Command(BaseCommand):
    help = 'Load sample Norwegian lesson data for portfolio demonstration'
    
    def handle(self, *args, **options):
        self.stdout.write('Loading sample Norwegian lesson data...')
        
        # A1 Level Lessons
        lesson_a1_greetings = Lesson.objects.create(
            title="Basic Greetings",
            cefr_level="A1",
            lesson_type="vocabulary",
            difficulty_score=1,
            estimated_duration=15,
            content_json={
                "introduction": "Learn essential Norwegian greetings for daily interactions",
                "vocabulary": [
                    {"norwegian": "Hei", "english": "Hello", "pronunciation": "hi"},
                    {"norwegian": "Ha det", "english": "Goodbye", "pronunciation": "ha-de"},
                    {"norwegian": "Takk", "english": "Thanks", "pronunciation": "tahk"},
                    {"norwegian": "Unnskyld", "english": "Excuse me", "pronunciation": "oon-shil"}
                ],
                "cultural_note": "Norwegians value politeness but are generally informal in greetings"
            }
        )
        
        Quiz.objects.create(
            lesson=lesson_a1_greetings,
            question_text="How do you say 'Hello' in Norwegian?",
            question_type="multiple_choice",
            correct_answer="Hei",
            options_json=["Hei", "Ha det", "Takk", "Unnskyld"]
        )
        
        lesson_a1_numbers = Lesson.objects.create(
            title="Numbers 1-20",
            cefr_level="A1",
            lesson_type="vocabulary",
            difficulty_score=2,
            estimated_duration=20,
            content_json={
                "introduction": "Master basic Norwegian numbers for everyday situations",
                "vocabulary": [
                    {"norwegian": "en/ett", "english": "one", "pronunciation": "en/et"},
                    {"norwegian": "to", "english": "two", "pronunciation": "too"},
                    {"norwegian": "tre", "english": "three", "pronunciation": "treh"},
                    {"norwegian": "fire", "english": "four", "pronunciation": "fee-reh"},
                    {"norwegian": "fem", "english": "five", "pronunciation": "fem"}
                ]
            }
        )
        
        # A2 Level Lessons
        lesson_a2_family = Lesson.objects.create(
            title="Family Members",
            cefr_level="A2",
            lesson_type="vocabulary",
            difficulty_score=3,
            estimated_duration=25,
            prerequisites=[lesson_a1_greetings.id],
            content_json={
                "introduction": "Learn to talk about your family in Norwegian",
                "vocabulary": [
                    {"norwegian": "familie", "english": "family", "pronunciation": "fah-mee-lee-eh"},
                    {"norwegian": "mor", "english": "mother", "pronunciation": "moor"},
                    {"norwegian": "far", "english": "father", "pronunciation": "fahr"},
                    {"norwegian": "søster", "english": "sister", "pronunciation": "surs-ter"},
                    {"norwegian": "bror", "english": "brother", "pronunciation": "broor"}
                ]
            }
        )
        
        lesson_a2_workplace = Lesson.objects.create(
            title="Workplace Basics",
            cefr_level="A2",
            lesson_type="vocabulary",
            difficulty_score=4,
            estimated_duration=30,
            content_json={
                "introduction": "Essential Norwegian for workplace communication",
                "vocabulary": [
                    {"norwegian": "jobb", "english": "job", "pronunciation": "yob"},
                    {"norwegian": "kollega", "english": "colleague", "pronunciation": "kol-leh-gah"},
                    {"norwegian": "møte", "english": "meeting", "pronunciation": "mur-teh"},
                    {"norwegian": "pause", "english": "break", "pronunciation": "pow-seh"}
                ],
                "cultural_note": "Norwegian workplaces emphasize equality and work-life balance"
            }
        )
        
        # B1 Level Lessons
        lesson_b1_grammar = Lesson.objects.create(
            title="Present Tense Verbs",
            cefr_level="B1",
            lesson_type="grammar",
            difficulty_score=5,
            estimated_duration=35,
            prerequisites=[lesson_a2_family.id],
            content_json={
                "introduction": "Master Norwegian present tense verb conjugations",
                "grammar_rules": [
                    {"rule": "Most verbs add -r in present tense", "example": "snakke → snakker (to speak → speaks)"},
                    {"rule": "Some verbs are irregular", "example": "være → er (to be → is)"}
                ],
                "examples": [
                    {"norwegian": "Jeg snakker norsk", "english": "I speak Norwegian"},
                    {"norwegian": "Hun arbeider her", "english": "She works here"}
                ]
            }
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded sample lesson data'))
        self.stdout.write(f'Created {Lesson.objects.count()} lessons across CEFR levels A1-B1')