from django.shortcuts import render, redirect
from .models import Reviews
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def dispReview(request):
    review = Reviews.objects.all()
    return render(request, 'review.html', {'review': review})

def addReview(request):
    if request.method == 'POST':
        desc = request.POST.get('desc')
        review = Reviews(desc=desc, uname=request.user)
        review.save()
        review = Reviews.objects.all()  # Fetch all reviews again
        return render(request, 'review.html', {'review': review})
    else:
        return render(request, 'review.html')

def deleteReview(request, review_id):
    review = get_object_or_404(Reviews, pk=review_id)
    if request.method == 'POST':
        # Check if the user is authorized to delete the review
        if request.user == review.uname:
            review.delete()
    return redirect('userreviewapp:dispReview')