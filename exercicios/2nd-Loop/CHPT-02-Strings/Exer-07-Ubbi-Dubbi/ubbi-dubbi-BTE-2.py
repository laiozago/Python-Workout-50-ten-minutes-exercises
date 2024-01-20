"""
Remove author names—In academia, it’s common to remove the authors’ names
from a paper submitted for peer review. Given a string containing an article and
a separate list of strings containing authors’ names, replace all names in the
article with _ characters.
"""


def remove_author_names(article, authors_list):
    for author_name in authors_list:
        article = article.replace(author_name, '_' * len(author_name))
    return article


# Example article
article_text = """
Title: The Impact of Technology on Society

Abstract:
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
In recent years, technological advancements have played a pivotal role in shaping society. 
John Doe and Jane Smith, in their collaborative effort, have explored the multifaceted effects 
of technology on various aspects of our lives.

Introduction:
John Doe, a renowned expert in artificial intelligence, and Jane Smith, a leading researcher 
in human-computer interaction, joined forces to investigate the societal impact of technology. 
Their research delves into the ways in which technological innovations have influenced 
communication, education, and work environments.

Body:
The study conducted by Doe and Smith encompasses a broad spectrum of technologies, 
ranging from artificial intelligence and robotics to the ubiquitous presence of smartphones. 
Their findings highlight the positive aspects of technology, such as improved efficiency 
and accessibility, as well as the challenges, including concerns about privacy and job displacement.

Conclusion:
In conclusion, the collaborative work of John Doe and Jane Smith sheds light on the complex 
relationship between technology and society. As we continue to embrace technological advancements, 
it is crucial to address the associated ethical and societal implications. 
The research encourages ongoing dialogue and reflection on how we can harness technology 
for the betterment of humanity while mitigating potential drawbacks.

Acknowledgments:
The authors would like to express their gratitude to the research participants 
and institutions that supported this study.

"""

authors_to_remove = ["John Doe", "Jane Smith"]

resulting_article = remove_author_names(article_text, authors_to_remove)
print(resulting_article)