import os
from app import create_app, db
from app.Model.models import ProgrammingLanguages, ResearchTopics, TechnicalElectives
# from app.Model.models import Post

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db} #'Post': Post}

@app.before_first_request
def initDB(*args, **kwargs):
    db.create_all()
    
    # Hard coded contents for certain db model.
    if ProgrammingLanguages.query.count() == 0:
        languages = ['Java', 'C#', 'C', 'C++', 'Python', 'R', 'Golang', 'Haskell', 'Swift', 'JavaScript', 'MATLAB', 'PHP',
                           'Ruby', 'Delphi', 'SQL']
    
        for pl in languages :
            db.session.add(ProgrammingLanguages(name=pl))
        db.session.commit()
    
    if ResearchTopics.query.count() == 0:
        # current available research area at WSU EECS
        researchtopics = ['Electronic Design Automation', 'High Performance Computing (HPC) and Scalable Data Science', 'Artificial Intelligence and Machine Learning',
                      'Bioinformatics', 'Distributed and Networked Systems', 'Power Engineering', 'Systems Engineering', 'Software Engineering']
        for rt in researchtopics:
            db.session.add(ResearchTopics(title=rt))
        db.session.commit()

    if TechnicalElectives.query.count() == 0:
        electives = ['Test1','Test2','Test3']

        for te in electives:
            db.session.add(TechnicalElectives(title=te))
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)