from jinja2 import Environment, FileSystemLoader
import scss


### Setup environment for jinja(jade) and SCSS
# Jinja with jade template system
env = Environment(
    loader        = FileSystemLoader('.'),
    extensions    = ['pyjade.ext.jinja.PyJadeExtension'],
    trim_blocks   = True,
    lstrip_blocks = True
    )

# Pyscss
# sass = scss.Scss(scss_opts={'style': 'compressed'} )
sass = scss.Scss()



### Compile

# Render subpages
about = {
    'id'      : 'about',
    'title'   : 'About',
    'content' : env.get_template('subpages/about.jade').render()
    }

research = {
    'id': 'research',
    'title': 'Research',
    'content' : env.get_template('subpages/research.jade').render()
    }

publication = {
    'id': 'publication',
    'title': 'Publication',
    'content' : ''
    }

# Interest

# Generate index.html
index_template = env.get_template('index.jade')
index_html = index_template.render(
    name = 'Tony Wu',
    sections = [
        about,
        research
        ]
    )

with open('../index.html', 'wb') as index_file:
    index_file.write(index_html)



# Compile Sass
main_css = sass.compile(scss_file = 'main.sass')
with open('../css/main.css', 'wb') as main_css_file:
    main_css_file.write(main_css)
