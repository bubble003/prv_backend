def object_details(request,id):

	obj = get_object_or_404(Post,id=id)
	viewed_by_session_count(request,obj)
	return redirect('/')