from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Section, Question, Option, UserAnswer, UserScore

def welcome_page(request):
    return render(request, 'aptitude_test/welcome.html')

def thank_you_page(request, total_score):
    context = {
        'total_score': total_score,
    }
    return render(request, 'aptitude_test/thank-you.html', context)

def quiz_view(request):
    user = request.user  # Assuming users are authenticated

    # Fetch all sections and their associated questions
    sections = Section.objects.prefetch_related('question_set').all()

    # Fetch the user's scores for each section
    user_scores = UserScore.objects.filter(user=user)

    # Create a dictionary to store scores for each section
    section_scores = {score.section_id: score.score for score in user_scores}

    context = {
        'sections': sections,
        'section_scores': section_scores,  # Pass the scores to the template
    }
    return render(request, 'aptitude_test/quiz.html', context)
def quiz_submit(request):
    if request.method == 'POST':
        user = request.user  # Assuming users are authenticated
        sections = Section.objects.all()

        total_score = 0  # Initialize total score

        for section in sections:
            for question in section.question_set.all():
                selected_option_id = request.POST.get(f'selected_option_{question.id}', None)

                if selected_option_id is not None:
                    selected_option = Option.objects.get(id=selected_option_id)

                    # Calculate the score for the question (1 point for correct answer)
                    if selected_option.is_correct:
                        score = 1
                    else:
                        score = 0

                    total_score += score  # Add score to the total score

                    # Create a UserAnswer record to store the user's answer
                    user_answer = UserAnswer(user=user, question=question, selected_option=selected_option)
                    user_answer.save()

        # Redirect to the "Thank You" page, passing the total score as a parameter
        return redirect('thank_you_page', total_score=total_score)

    return redirect('quiz')  # Redirect to the quiz page if there's an issue with the request
