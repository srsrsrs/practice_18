from common_config import headers,cookies
import requests
from bs4 import BeautifulSoup
import json


def read_questions(question_id):
    url = "https://www.zhihu.com/api/v4/questions/{}/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].mark_infos[*].url;data[*].author.follower_count,badge[?(type=best_answerer)].topics&limit=10&offset=0&sort_by=default".format(question_id)
    s = requests.session()
    homeReq = s.get(url, headers=headers,cookies=cookies)
    homeSoup = BeautifulSoup(homeReq.text, 'lxml')
    s.close()
    return homeSoup


def convert_soup_to_json(soup):
    return json.loads(soup.p.text)


if __name__=='__main__':
    soup = read_questions(287430572)
    print(soup)
