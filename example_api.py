import falcon


class CORSMiddleware:
    origin = "falconframework.org"

    def process_response(self, req, resp, *args, **kwargs):
        resp.set_header("Access-Control-Allow-Origin", self.origin)

    def process_request(self, req, resp):
        assert req.headers["ORIGIN"] == self.origin


api = falcon.API()
cors_api = falcon.API(middleware=[CORSMiddleware()])


class ExampleResource:
    def on_get(self, request, response, id):
        if id == 20:
            response.media, response.status = "20 ok", falcon.HTTP_200
        else:
            response.media, response.status = "Invalid id", falcon.HTTP_400

    def on_post(self, request, response):
        if request.media == {"id": 42}:
            response.media, response.status = "42 created", falcon.HTTP_201
        else:
            response.media, response.status = "Invalid id", falcon.HTTP_400

    def on_put(self, request, response, id):
        if id == 20:
            response.media, response.status = "20 updated", falcon.HTTP_200
        elif id == 24:
            response.status = falcon.HTTP_204
        else:
            response.media, response.status = "Invalid id", falcon.HTTP_400

    def on_delete(self, request, response, id):
        if id == 20:
            response.media, response.status = "20 deleted", falcon.HTTP_200
        elif id == 24:
            response.status = falcon.HTTP_204
        elif id == 22:
            response.media, response.status = "22 accepted", falcon.HTTP_202
        else:
            response.media, response.status = "Invalid id", falcon.HTTP_400

    def on_head(self, request, response, id):
        if id == 20:
            response.status = falcon.HTTP_200
        else:
            response.status = falcon.HTTP_400


example_resource = ExampleResource()

api.add_route("/example/", example_resource)
api.add_route("/example/{id:int}/", example_resource)

cors_api.add_route("/example/", example_resource)
cors_api.add_route("/example/{id:int}/", example_resource)
