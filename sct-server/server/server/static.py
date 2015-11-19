from pyramid.static import static_view
static_view = static_view('app:./', use_subpath=True)
