from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Tag


def parse_tags(tags_text):
    if not tags_text:
        return []
    names = [name.strip() for name in tags_text.split(',')]
    names = [name for name in names if name]
    tags = []
    for name in names:
        tag, created = Tag.objects.get_or_create(title=name)
        tags.append(tag)
    return tags


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tags = parse_tags(request.POST.get('tags'))

        note = Note(title=title, content=content)
        note.save()
        note.tags.set(tags)
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete_note(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        Note.objects.filter(id=note_id).delete()
    return redirect('index')

def edit_note(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        note = get_object_or_404(Note, id=note_id)

        if 'titulo' in request.POST:
            note.title = request.POST.get('titulo')
            note.content = request.POST.get('detalhes')
            note.save()
            note.tags.set(parse_tags(request.POST.get('tags')))
            return redirect('index')

        tags_str = ', '.join(tag.title for tag in note.tags.all())
        return render(request, 'notes/edit.html', {'note': note, 'tags_str': tags_str})
    return redirect('index')

def tags_list(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': all_tags})

def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    notes_with_tag = Note.objects.filter(tags=tag)
    return render(request, 'notes/tag_detail.html', {'tag': tag, 'notes': notes_with_tag})