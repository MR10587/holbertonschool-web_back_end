const app = require("./api");
const { expect } = require("chai");
const request = require("supertest");

describe("Route test for index page", () => {
  it("returns correct status code", (done) => {
    request(app)
      .get("/")
      .end((err, res) => {
        if (err) return done(err);
        expect(res.statusCode).to.equal(200);
        done();
      });
  });

  it("returns correct response body", (done) => {
    request(app)
      .get("/")
      .end((err, res) => {
        if (err) return done(err);
        expect(res.text).to.equal("Welcome to the payment system");
        done();
      });
  });

  it("returns correct status code for number id", (done) => {
    request(app)
      .get("/card/1")
      .end((err, res) => {
        if (err) return done(err);
        expect(res.statusCode).to.equal(200);
        expect(res.text).to.equal("Payment methods for card 1");
        done();
      });
  });

  it("returns correct status code for non-number id", (done) => {
    request(app)
      .get("/card/abc")
      .end((err, res) => {
        if (err) return done(err);
        expect(res.statusCode).to.equal(404);
        done();
      });
  });
});
