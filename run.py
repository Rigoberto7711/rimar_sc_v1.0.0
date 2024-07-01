from app import create_app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        print("\n".join([str(rule) for rule in app.url_map.iter_rules()]))
    app.run(debug=True)
