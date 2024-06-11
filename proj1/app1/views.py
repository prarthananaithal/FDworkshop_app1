from django.shortcuts import render


# Create your views here.
def find_substring_combinations(word):
    if len(word) == 1:
        return [word]
    combinations = []
    for i, char in enumerate(word):
        rest = word[:i] + word[i+1:]
        for combo in find_substring_combinations(rest):
            combinations.append(char + combo)
    return combinations

def substring_view(request):
    combinations = []
    if request.method == 'GET':
        word = request.GET.get('word', '')
        if word:
            combinations = find_substring_combinations(word)
    return render(request, 'app1/index.html', {'combinations': combinations})
            


    
    


