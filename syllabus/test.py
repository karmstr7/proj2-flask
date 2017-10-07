import pre
import config
import arrow

configuration = config.configuration()

syllabus = pre.process(open(configuration.SYLLABUS, encoding="utf-8"))
beginning_date = pre.base


def mark_week(w):
    dict_count = 1
    count = 0
    new_dict = {}
    for i in w:
        week_i = beginning_date.replace(days=count).format("MM/DD")
        i['week'] += " {}".format(week_i)
        count += 7
        new_dict['{}'.format(dict_count)] = i['week']
        dict_count += 1
    print(new_dict)
if __name__ == "__main__":
    mark_week(syllabus)