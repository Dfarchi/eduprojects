# import requests as requests
#
#
# class VTMngr:
#      def __init__(self):
#          pass
#
#      def get_url_analysis(self, url):
#
#          response = requests.get(url)
#          if response.status_code == 400:
#              # unknown error
#              raise Exception("cannot get to api")
#          elif response.status_code == 402:
#              # too many requests, try later
#              # write a lot of code that continues the run
#              pass
#      def get_urls(self, urls):
#          results = []
#          for url in urls:
#              try:
#                  response = requests.get(url)
#                  results.append(response)
#              except:
#                  results.append("failed")
#          if all([res=='failed' for res in results]):
#              raise Exception("Everything failed")
#          else:
#              return results
#
#
#
#
#
#
#
#
# if __name__ == '__main__':
#     mngr = VTMngr()
#     try:
#         mngr.get_url_analysis("https:/fgdgs")
#     except:
#         #